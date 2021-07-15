import numpy as np


def reorder(a, b):
    return np.roll(np.arange(a).reshape(2, -1), b, 1).tolist()

