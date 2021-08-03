def year_days(year):
    s = 1
    if year % 100 == 0:
        if year % 400 == 0:
            s = 1
        else:
            s = 0
    return '{} has 366 days'.format(year) if year % 4 == 0 and s else '{} has 365 days'.format(year)
