import numpy as np
from scipy import ndimage


def advice(agents, n):
    town = np.ones((n, n)) if n else np.zeros((1, 1))
    for (x, y) in agents:
        if x < n and y < n:
            town[x, y] = 0
    d = ndimage.distance_transform_cdt(town, metric='taxicab')
    return list(zip(*np.where(d == d.max()))) if d.max() else []
