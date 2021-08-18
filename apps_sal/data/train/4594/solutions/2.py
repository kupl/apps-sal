import numpy as np


def transpose(matrix):
    return list(map(list, zip(*matrix)))
    return np.transpose(matrix).tolist()
