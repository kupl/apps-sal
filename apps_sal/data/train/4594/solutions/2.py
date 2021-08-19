import numpy as np

# Take your pick


def transpose(matrix):
    return list(map(list, zip(*matrix)))
    return np.transpose(matrix).tolist()
