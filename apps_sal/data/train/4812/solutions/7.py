from math import ceil


def nth_floyd(t):
    return ceil((-1 + (1 + 8 * t) ** 0.5) / 2)
