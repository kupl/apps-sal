import math


def round_it(n):
    a = str(n)
    b = a.find('.')
    if len(a) / 2 - 1 >= b:
        return math.ceil(n)
    elif len(a) / 2 <= b:
        return math.floor(n)
    else:
        return round(n)
