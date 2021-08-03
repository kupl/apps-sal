import math


def century(year):
    # Finish this :)
    # if no remainder when dividing by 100, return result of division
    if year % 100 == 0:
        return year / 100
    # if remainder when dividing by 100, return result of division rounded up to nearest whole number
    else:
        return math.ceil(year / 100)
    return
