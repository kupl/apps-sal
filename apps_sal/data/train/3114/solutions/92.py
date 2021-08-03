def year_days(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return f'{year} has 366 days'
        else:
            return f'{year} has 365 days'
    else:
        return f'{year} has 366 days' if year % 4 == 0 else f'{year} has 365 days'
