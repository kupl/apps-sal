import numpy as np


def round_to_next5(n):
    if np.int(n / 5) * 5 == n:
        return n
    if np.int(n / 5) * 5 != n:
        return np.int(n / 5) * 5 + 5 * (n > 0)
