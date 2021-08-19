def year_days(year):
    d = 0
    if int(year % 400) == 0:
        d = 366
    elif int(year % 4) == 0 and int(year % 100) != 0:
        d = 366
    else:
        d = 365
    return '{} has {} days'.format(year, d)
