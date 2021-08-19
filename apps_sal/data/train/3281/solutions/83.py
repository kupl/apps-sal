from datetime import datetime


def unlucky_days(year: int) -> sum:
    return sum((datetime(year, month, 13).weekday() == 4 for month in range(1, 13)))
