from math import sqrt, ceil


def group_size(s, d):
    n = ceil((1 - 2 * s + sqrt((2 * s - 1)**2 + 8 * d)) / 2)
    return s + n - 1
