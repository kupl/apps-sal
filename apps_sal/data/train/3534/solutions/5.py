import numpy as np


def to_bits(string):
    arr = [int(s) for s in string.split('\n')]
    bm = np.zeros(5000)
    for i in arr:
        bm[i] += 1 * (1 - bm[i])
    return list(bm)
