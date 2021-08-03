from math import log10, floor, pi, e


def count(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    x = n * log10(n / e) + log10(2 * pi * n) / 2
    return floor(x) + 1
