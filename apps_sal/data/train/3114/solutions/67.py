def year_days(year):
    if year / 100 % 1 == 0:
        if year / 400 % 1 == 0:
            return str(year) + ' has 366 days'
        else:
            return str(year) + ' has 365 days'
    return str(year) + ' has 366 days' if year / 4 % 1 == 0 else str(year) + ' has 365 days'
