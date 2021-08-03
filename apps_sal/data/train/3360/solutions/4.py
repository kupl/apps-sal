import numpy as np


def get_chance(n, x, a):
    ns = np.arange(n, n - a, -1)
    return np.multiply.reduce((ns - x) / ns).round(2)
