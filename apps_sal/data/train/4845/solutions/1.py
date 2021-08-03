import numpy as np


def sort_nested_list(A):
    return np.sort(A, axis=None).reshape(np.array(A).shape).tolist()
