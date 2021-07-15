def year_days(year):
    leap = (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)
    return '{} has {} days'.format(year, 366 if leap else 365)
