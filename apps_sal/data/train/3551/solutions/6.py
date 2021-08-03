import numpy as np


def array_previous_less(arr):
    arr = arr[::-1]
    output = np.full(len(arr), -1)
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            if j < arr[i]:
                output[i] = j
                break
    return output.tolist()[::-1]
