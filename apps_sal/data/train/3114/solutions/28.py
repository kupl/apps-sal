def year_days(year):
    is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    return f'{year} has {365 + int(is_leap_year)} days'
