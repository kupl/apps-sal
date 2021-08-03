import numpy as np


def find_difference(a, b):
    return abs(np.multiply.reduce(a) - np.multiply.reduce(b))
