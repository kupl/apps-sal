import numpy as np


def box_force(k, n):
    return 1 / (k * (n + 1) ** (2 * k))


def doubles(maxk, maxn):
    return np.fromfunction(lambda i, j: box_force(i + 1, j + 1), (maxk, maxn)).sum()
