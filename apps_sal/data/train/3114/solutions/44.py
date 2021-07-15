def year_days(year):
    if not year%400:
        return f'{year} has 366 days'
    if not year%4 and year%100:
        return f'{year} has 366 days'
    return f'{year} has 365 days'
