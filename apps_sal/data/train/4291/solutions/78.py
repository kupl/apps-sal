import math


def century(year):
    if year % 100 == 0:
        return year / 100
    else:
        return math.ceil(year / 100)
    return
