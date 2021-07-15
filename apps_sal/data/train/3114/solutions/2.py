def year_days(year):
    return '{} has {} days'.format(year, 366 if year % 400 == 0 or (year % 4 == 0 and year % 100) else 365)
