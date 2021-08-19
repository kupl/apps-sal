from math import log


def compare(x, y):
    if x == y:
        return 0
    if x < y:
        return 1
    if x > y:
        return -1


def compare_powers(x, y):
    (a, c) = x
    (b, d) = y
    x = c * log(a) / log(2)
    y = d * log(b) / log(2)
    return compare(x, y)
