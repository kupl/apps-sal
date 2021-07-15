def year_days(year):
    return f'{year} has 366 days' if year == 0 or (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else f'{year} has 365 days'
