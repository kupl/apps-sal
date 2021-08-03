import numpy as np


def find_all(array, n):
    return list(np.where(np.array(array) == n)[0])
