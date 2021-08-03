import datetime


def unlucky_days(year):
    cnt = 0
    for i in range(1, 13):
        d = datetime.datetime(year, i, 13)
        if d.weekday() == 4:
            cnt += 1
    return cnt
