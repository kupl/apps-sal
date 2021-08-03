def year_days(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return str(year) + ' has 365 days'
    else:
        return str(year) + ' has 366 days' if year % 4 == 0 else str(year) + ' has 365 days'
