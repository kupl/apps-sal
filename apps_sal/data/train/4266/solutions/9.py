import numpy as np


def min_dot(a, b):
    return np.dot(sorted(a), sorted(b, reverse=True))
