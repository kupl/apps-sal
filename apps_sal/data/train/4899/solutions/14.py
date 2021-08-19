from math import exp


def weight(N, w):
    return sum((0.25 * exp(-2 * (n + 1)) * (exp(2) - 3) for n in range(N))) * w
