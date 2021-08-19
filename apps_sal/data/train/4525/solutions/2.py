from calendar import month_name
months = {m: i for (i, m) in enumerate(month_name)}


def check_challenge(pledged, current, month):
    if pledged == current:
        return 'Challenge is completed.'
    (q, r) = divmod(pledged, 12)
    m = months[month] - 1
    val = current - m * q - min(m, r)
    if m and val:
        return f'You are {-val} behind schedule.' if val < 0 else f'You are {val} ahead of schedule!'
    return 'You are on track.'
