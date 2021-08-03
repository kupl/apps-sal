import datetime


def unlucky_days(year):
    return sum(datetime.datetime(year, m + 1, 13).weekday() == 4 for m in range(12))
