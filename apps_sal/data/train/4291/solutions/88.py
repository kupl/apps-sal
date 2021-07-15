import math

def century(year):
    if 100 >= year >= 1:
        return 1
    elif year % 2 == 0:
        return math.ceil(year / 100)
    else:
        return year // 100 + 1
