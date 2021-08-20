import numpy as np


def hyperrectangularity_properties(arr):
    try:
        return np.shape(arr) if np.array(arr).dtype.char != 'O' else None
    except ValueError:
        return None
