import calendar

def year_days(year):
    if calendar.isleap(year):
        return '{0} has 366 days'.format(year)
    else:
        return '{0} has 365 days'.format(year)
