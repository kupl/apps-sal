def year_days(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return '{} has {} days'.format(year, 366)
        else:
            return '{} has {} days'.format(year, 365)
    if year % 4 == 0:
        return '{} has {} days'.format(year, 366)
    else:
        return '{} has {} days'.format(year, 365)
