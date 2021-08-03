import datetime


def unlucky_days(year):
    return sum([1 for m in range(1, 13) if datetime.date(year, m, 13).weekday() == 4])
