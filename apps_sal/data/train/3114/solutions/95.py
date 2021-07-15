def year_days(year):
    num_days = 365
    if year % 100 == 0:
        if (year / 100) % 4 == 0:
            num_days = 366
    elif year % 4 == 0:
        num_days = 366
    
    return '{} has {} days'.format(year, num_days)
