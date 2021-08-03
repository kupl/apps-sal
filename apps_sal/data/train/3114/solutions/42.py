import calendar


def year_days(year):
    return '{} has 366 days'.format(year) if calendar.isleap(year) else '{} has 365 days'.format(year)
