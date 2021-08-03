def year_days(year):
    x = 366 if year % 4 == 0 else 365
    if year % 100 == 0 and year % 400 != 0:
        x = 365
    return f'{year} has {x} days'
