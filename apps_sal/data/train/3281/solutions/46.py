import datetime


def unlucky_days(n):
    c = 0
    d = datetime.timedelta(days=1)
    t = datetime.date(n, 1, 1)
    while t != datetime.date(n, 12, 31):
        if t.day == 13 and t.strftime('%A') == 'Friday':
            c = c + 1
        t = t + d
    return c
