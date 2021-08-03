from datetime import *


def julian(day, month, year):
    dayy = (year - 1) * 365 + (year - 1) // 4
    daym = sum([0, 31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month])
    return dayy + daym + day


ref = date(2437, 3, 24)
greg = date(1752, 9, 14)
days2greg = (ref - greg).days
jgreg = julian(3, 9, 1752)


def days(day, month, year):
    if year > 1752 or (year == 1752 and month > 9) or (year == 1752 and month == 9 and day > 13):
        return (ref - date(year, month, day)).days
    else:
        return jgreg - julian(day, month, year) + days2greg
