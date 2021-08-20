def year_days(year):
    return '{} has 365 days'.format(year) if year % 4 != 0 else '{} has 365 days'.format(year) if year % 100 == 0 and year % 400 != 0 else '{} has 366 days'.format(year)
