def year_days(y):
    days = 365
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        days = days + 1
    return '{} has {} days'.format(y, days)
