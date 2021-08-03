def year_days(year):

    if str(year)[-2:] == '00' and year % 400 != 0:
        return f'{year} has 365 days'
    if str(year)[-2:] == '00' and year % 400 == 0:
        return f'{year} has 366 days'

    if year % 4 == 0:
        return f'{year} has 366 days'

    return f'{year} has 365 days'
