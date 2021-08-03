import numpy as np


def symmetric_point(p, q):
    npp = np.array(p)
    npq = np.array(q)
    return (npq - npp + npq).tolist()
