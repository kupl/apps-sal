from datetime import date


def unlucky_days(year):
    return sum((date(year, months, 13).weekday() == 4 for months in range(1, 13)))
