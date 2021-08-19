import numpy as np


def performant_smallest(a, n):
    l = len(a)
    arr = np.array([v + i / l for (i, v) in enumerate(a)])
    ag = np.argpartition(arr, n - 1)
    args = np.sort(ag[:n])
    return [a[x] for x in args]
