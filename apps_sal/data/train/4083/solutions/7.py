import numpy as np

def performant_smallest(arr, n):
    return np.asarray(arr)[np.sort(np.argsort(arr, kind='mergesort')[:n])].tolist()
