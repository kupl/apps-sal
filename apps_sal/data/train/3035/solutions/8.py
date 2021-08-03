import numpy as np


def getMatrixProduct(a, b):
    try:
        return np.dot(a, b).tolist()
    except:
        return -1
