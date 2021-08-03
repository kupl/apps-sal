import math


def approx_root(n):
    a = n ** 0.5
    b, c = math.floor(a) ** 2, (math.floor(a) + 1) ** 2
    return a if type(a) == int else round(b ** 0.5 + (n - b) / (c - b), 2)
