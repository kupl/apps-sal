def year_days(year):
    return "{} has {} days".format(year, 366 if (not year % 100 and not year % 400) or (not year % 4 and year % 100) else 365)
    # your code here
