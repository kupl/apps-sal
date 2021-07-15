import numpy as np

def circular_limited_sums(max_n, max_fn):
    if max_n == 1: return max_fn//2 + 1
    if max_n == 2: return ((max_fn+1) * (max_fn+2))//2
    t = np.matrix(np.flipud(np.tri(max_fn+1, max_fn+1, 0, object)))
    k = t ** (max_n-2)
    return (np.sum(k.dot(np.arange(max_fn+1, 0, -1)[:, None])) - np.sum(np.multiply(k.dot(t), np.logical_not(t)))) % 12345787
