import numpy as np


def matrix_mult(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.matmul(a, b).tolist()
