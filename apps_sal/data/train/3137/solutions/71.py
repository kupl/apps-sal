import math


def round_it(n):
    print(n)
    x = str(n).split('.')
    if len(x[0]) < len(x[1]):
        return math.ceil(n)
    elif len(x[0]) > len(x[1]):
        return math.floor(n)
    else:
        return round(n)
