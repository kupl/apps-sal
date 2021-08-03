from math import sqrt


def is_triangular(t):
    n = (sqrt(8 * t + 1) - 1) / 2
    return False if n - int(n) > 0 else True
