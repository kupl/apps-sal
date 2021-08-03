import numpy as np


def snail(array):
    arr = np.array(array)

    if len(arr) < 2:
        return arr.flatten().tolist()

    tp = arr[0, :].tolist()
    rt = arr[1:, -1].tolist()
    bm = arr[-1:, :-1].flatten()[::-1].tolist()
    lt = arr[1:-1, 0][::-1].tolist()

    return tp + rt + bm + lt + snail(arr[1:-1, 1:-1])
