import math


def round_it(n):
    val = str(n).split('.')
    if len(val[0]) > len(val[1]):
        return math.floor(n)
    elif len(val[0]) < len(val[1]):
        return math.ceil(n)
    else:
        return round(n)
