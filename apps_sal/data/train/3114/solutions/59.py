def year_days(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    if leap:
        days = 366
    else:
        days = 365
    return f'{year} has {days} days'
