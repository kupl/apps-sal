import numpy as np


def bar_triang(pointA, pointB, pointC):
    return [np.round((pointA[0] + pointB[0] + pointC[0]) / 3, 4), np.round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)]
