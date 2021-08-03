import numpy as np


def getMatrixProduct(a, b):
    try:
        return (np.matrix(a) * np.matrix(b)).tolist()
    except ValueError:
        return -1
