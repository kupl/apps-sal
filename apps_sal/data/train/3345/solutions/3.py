import numpy as np


def find_uniq(arr):
    arr1 = [''.join(sorted(set(i.lower().replace(' ', '')))) for i in arr]
    lst = np.unique(arr1)
    for i in lst:
        if arr1.count(i) == 1:
            return arr[arr1.index(i)]
