import numpy as np


def find_difference(a, b):
    return max(np.prod(a) - np.prod(b), np.prod(b) - np.prod(a))
