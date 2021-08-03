import numpy as np


def merge_arrays(first, second):
    return sorted(np.unique(first + second))
