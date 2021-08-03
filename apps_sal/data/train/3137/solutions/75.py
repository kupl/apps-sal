import math


def round_it(n):
    x = len(str(int(n)))
    y = len(str(n)) - x - 1
    return math.ceil(n) if x < y else math.floor(n) if x > y else round(n)
