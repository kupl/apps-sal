def year_days(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return '%s has 366 days' % year
        else:
            return '%s has 365 days' % year
    else:
        return '%s has 366 days' % year if year % 4 == 0 else '%s has 365 days' % year
