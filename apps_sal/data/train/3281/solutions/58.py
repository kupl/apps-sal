import calendar


def unlucky_days(year):
    return sum([calendar.weekday(year, month, 13) == 4 for month in range(1, 13)])
