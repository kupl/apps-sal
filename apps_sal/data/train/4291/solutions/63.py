from math import *


def century(year):
    if str(year)[-2:] == "00":
        year = year - 1
    return floor(year / 100) + 1


date = 1900
print(century(date))
