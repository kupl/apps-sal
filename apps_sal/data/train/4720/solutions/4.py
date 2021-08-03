import numpy as np


def hyperrectangularity_properties(arr):
    try:
        arr = np.array(arr)
    except ValueError:
        return None
    return arr.shape if arr.dtype.char != 'O' else None
