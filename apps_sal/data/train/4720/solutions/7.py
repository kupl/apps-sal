import numpy as np


def hyperrectangularity_properties(arr):
    try:
        return None if np.array(arr).dtype == np.dtype("O") else np.shape(arr)
    except (ValueError):
        return None
