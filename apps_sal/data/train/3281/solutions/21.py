from datetime import datetime


def unlucky_days(year):
    return sum(datetime(year, a, 13).weekday() == 4 for a in range(1, 13))
