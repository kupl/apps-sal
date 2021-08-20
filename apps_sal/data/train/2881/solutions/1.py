import numpy as np


def validate(cc_number):
    arr = np.array([int(i) for i in str(cc_number)])
    arr[-2::-2] *= 2
    arr[arr > 9] -= 9
    return np.sum(arr) % 10 == 0
