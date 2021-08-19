
from calendar import isleap


def year_days(year):
    # print(isleap(year)) # gives 1 if it is leap year
    return "{} has {} days".format(year, isleap(year) + 365)
