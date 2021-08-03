def year_days(year):
    if abs(year) % 100 == 0:
        return f'{year} has 366 days' if abs(year) % 400 == 0 else f'{year} has 365 days'
    else:
        return f'{year} has 366 days' if abs(year) % 4 == 0 else f'{year} has 365 days'
