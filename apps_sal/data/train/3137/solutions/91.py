import math


def round_it(n):
    (x, y) = str(n).split('.')
    return round(n) if len(x) == len(y) else math.ceil(n) if len(x) < len(y) else math.floor(n)
