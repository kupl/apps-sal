def year_days(year):
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        return f'{year} has 366 days'
    else:
        return f'{year} has 365 days'
