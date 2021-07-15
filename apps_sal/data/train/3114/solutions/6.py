def year_days(year):
    x = 366 if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0 else 365
    return '%d has %d days' % (year, x)
        

