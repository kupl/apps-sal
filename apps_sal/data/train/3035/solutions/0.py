import numpy as np

def getMatrixProduct(a, b):
    try:
        return np.matmul(a, b).tolist()
    except:
        return - 1
