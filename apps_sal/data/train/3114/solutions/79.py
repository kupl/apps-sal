def year_days(year):
    msg = ' has 365 days'
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        msg = ' has 366 days'
    return str(year) + msg
