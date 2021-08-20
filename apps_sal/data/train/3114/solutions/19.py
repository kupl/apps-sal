from calendar import isleap


def year_days(year):
    if isleap(year):
        return '{} has 366 days'.format(year)
    return '{} has 365 days'.format(year)
