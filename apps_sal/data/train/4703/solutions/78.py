import numpy as np


def bar_triang(pointA, pointB, pointC):  # points A, B and C will never be aligned
    # your code here
    return [np.round((pointA[0] + pointB[0] + pointC[0]) / 3, 4), np.round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)]  # coordinates of the barycenter expressed up to four decimals
    # (rounded result)
