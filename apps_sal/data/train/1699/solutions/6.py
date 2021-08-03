import numpy as np


def get_v(k, n):
    return 1 / (k * np.power((n + 1).reshape(-1, 1), (2 * k).reshape(1, -1)))


def doubles(K, N):
    K = np.arange(1, K + 1, dtype=np.float64)
    N = np.arange(1, N + 1, dtype=np.float64)
    return get_v(K, N).sum()
