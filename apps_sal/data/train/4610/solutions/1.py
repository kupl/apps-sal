from math import log


def number_increasing(n):
    return any(log(x, 3).is_integer() for x in range(n, 0, -5))
