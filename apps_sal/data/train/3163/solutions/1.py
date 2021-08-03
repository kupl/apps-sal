from math import sqrt


def triangular_sum(n):
    return sqrt(2 * (sqrt(8 * n + 1) - 1)) % 2 == 0
