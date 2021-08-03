from math import exp


def weight(n, w):
    return w * (exp(2) - 3) * (1 - exp(-2 * n)) / (4 * (exp(2) - 1))
