from calendar import weekday


def unlucky_days(year):
    return sum((1 for i in range(1, 13) if weekday(year, i, 13) == 4))
