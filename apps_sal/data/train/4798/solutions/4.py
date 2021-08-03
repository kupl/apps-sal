import numpy as np


def avg_diags(arr):
    arr = np.array(arr)
    d1 = np.diag(arr)
    d2 = np.diag(np.flipud(arr))

    d1 = d1[1::2]
    d1 = d1[d1 >= 0].mean().round()

    d2 = d2[::2]
    d2 = abs(d2[d2 < 0].mean().round())

    d1 = -1 if np.isnan(d1) else d1
    d2 = -1 if np.isnan(d2) else d2
    return [d1, d2]
