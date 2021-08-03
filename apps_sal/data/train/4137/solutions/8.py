import math


def is_square(n):
    if n < 0:
        return False
    r = math.sqrt(n)
    r = math.floor(r)
    return r * r == n
