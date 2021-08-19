def year_days(year):
    days = 365 if year % 4 else 366 if year % 100 else 365 if year % 400 else 366
    return '{0} has {1} days'.format(year, days)
