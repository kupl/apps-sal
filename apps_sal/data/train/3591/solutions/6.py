import numpy as np


def doors(n):
    doors = np.zeros(n, dtype=int)
    for i in range(n):
        doors[i::i + 1] ^= 1
    return sum(doors)
