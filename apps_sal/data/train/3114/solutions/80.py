def year_days(year):
    
    abs_year = abs(year)
    leap_year = ' has 365 days'
    
    if abs_year % 100 == 0 and abs_year % 400 == 0:
        leap_year = ' has 366 days'
    elif abs_year % 100 != 0 and abs_year % 4 == 0:
        leap_year = ' has 366 days'
    
    return str(year) + leap_year
