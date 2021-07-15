def year_days(year):
    return "%d has %d days" % (year, 365 + (not year % 400 if not year % 100 else not year % 4))
