import numpy as np


def transpose(A):
    if len(A) == 0:
        return []
    return np.array(A, dtype='O').T.tolist() if len(A[0]) > 0 else [[]]
