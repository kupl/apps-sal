from datetime import datetime


def unlucky_days(year):
    return sum(map(lambda i: datetime(year, i, 13).weekday() == 4, [i for i in range(1, 13)]))
