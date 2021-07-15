import numpy as np

def sort_two_arrays(arr1, arr2):
    idx2 = np.argsort(arr2, kind='mergesort')
    idx1 = np.argsort(arr1, kind='mergesort')
    return [[arr1[i] for i in idx2], [arr2[i] for i in idx1]]
