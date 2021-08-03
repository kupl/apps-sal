import calendar


def unlucky_days(year):
    return [calendar.weekday(year, x + 1, 13) for x in range(12)].count(4)
