import math


def round_it(n):
    l = str(n).split('.')
    x = len(l[0])
    y = len(l[1])
    return math.ceil(n) if x < y else math.floor(n) if x > y else round(n)
