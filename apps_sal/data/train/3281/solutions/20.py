from datetime import datetime


def unlucky_days(year):
    return sum(True for month in range(1, 13) if datetime(year=year, month=month, day=13).weekday() == 4)
