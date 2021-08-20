def year_days(year):
    leap = year % 4 == 0 and (not year % 100 == 0) or year % 400 == 0
    number_of_days = 365 if not leap else 366
    return '{} has {} days'.format(year, number_of_days)
