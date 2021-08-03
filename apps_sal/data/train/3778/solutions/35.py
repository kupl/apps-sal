import numpy as np


def find_smallest_int(arr):
    test = np.sort(arr)
    answer = int(test[0])
    return answer
