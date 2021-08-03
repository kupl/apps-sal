from math import exp


def weight(n, w):
    return w / 4 * (1 - 3 * exp(-2)) * (1 - exp(-2 * n - 4)) / (1 - exp(-2))
