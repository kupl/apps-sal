import math


def century(year):
    if year % 100 == 0:
        what_century = year / 100
    else:
        what_century = math.floor(year / 100) + 1
    return what_century
