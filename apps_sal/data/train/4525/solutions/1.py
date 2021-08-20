MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MONTHS_DCT = {m: i for (i, m) in enumerate(MONTHS)}


def check_challenge(pledged, current, month):
    if month == MONTHS[0]:
        return 'You are on track.'
    if current == pledged:
        return 'Challenge is completed.'
    (n, r) = divmod(pledged, 12)
    accum = sum((n + (i < r) for i in range(MONTHS_DCT[month])))
    delta = accum - current
    return 'You are on track.' if delta == 0 else 'You are {} behind schedule.'.format(delta) if delta > 0 else 'You are {} ahead of schedule!'.format(abs(delta))
