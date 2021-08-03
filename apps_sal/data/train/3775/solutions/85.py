import math


def digits(n):
    d = 1
    while n >= 10:
        d += 1
        n = math.floor(n / 10)
    return d
