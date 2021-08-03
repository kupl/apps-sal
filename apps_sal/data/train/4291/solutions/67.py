import math


def century(year):
    return math.floor(year / 100) + (year % 100 and 1)
