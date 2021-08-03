from math import log


def half_life(N0, N, t):
    return t / log(N0 / N, 2)
