def year_days(year):
    if year % 400 == 0:
        return str(year) + ' has 366 days'
    elif year % 100 == 0:
        return str(year) + ' has 365 days'
    if year % 4 == 0:
        return str(year) + ' has 366 days'
    else:
        return str(year) + ' has 365 days'
