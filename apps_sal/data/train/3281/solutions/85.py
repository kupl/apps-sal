from datetime import datetime


def unlucky_days(year):
    return sum(map(lambda x: datetime(year, x, 13).weekday() == 4, range(1, 13)))
