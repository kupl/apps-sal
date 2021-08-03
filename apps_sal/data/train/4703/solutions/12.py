import numpy as np


def bar_triang(*points):
    return np.mean(points, axis=0).round(4).tolist()
