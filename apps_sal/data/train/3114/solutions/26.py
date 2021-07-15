def year_days(year):
    days = 365
    if year % 100 == 0:
        if year % 400 == 0:
            days += 1
    elif year % 4 == 0:
        days += 1
    return f'{year} has {days} days'
