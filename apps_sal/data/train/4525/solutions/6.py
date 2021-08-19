from itertools import accumulate


def check_challenge(pledged, current, month):
    if month == 'January':
        return 'You are on track.'
    if pledged == current:
        return 'Challenge is completed.'
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    (q, r) = divmod(pledged, 12)
    progresses = list(accumulate([q + (m < r) for m in range(12)]))
    p = progresses[months.index(month) - 1]
    if p == current:
        return 'You are on track.'
    return f'You are {p - current} behind schedule.' if p > current else f'You are {current - p} ahead of schedule!'
