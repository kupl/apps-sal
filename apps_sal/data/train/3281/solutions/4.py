from datetime import date


def unlucky_days(year):
    return sum(1 for month in range(1, 13) if date(year, month, 13).weekday() == 4)
