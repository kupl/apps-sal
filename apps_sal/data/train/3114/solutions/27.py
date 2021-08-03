def year_days(year):
    if year == 0:
        days = 366
    elif year % 100 == 0 and year % 400 != 0:
        days = 365
    elif year % 4 != 0:
        days = 365
    else:
        days = 366
    return f"{year} has {days} days"
