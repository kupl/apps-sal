import datetime


def year_days(year):
    # your code here
    if year == 0:
        return f'{year} has 366 days'
    elif year % 400 == 0:
        return f'{year} has 366 days'
    elif year % 100 == 0:
        return f'{year} has 365 days'
    elif year % 4 == 0:
        return f'{year} has 366 days'
    else:
        return f'{year} has 365 days'
