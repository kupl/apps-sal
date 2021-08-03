import numpy as np


def reorder(a, b):
    if a % 2:
        m = a // 2
        new_array = np.array([number for number in range(0, a)])
        c = np.array_split(new_array, len(new_array) / m)
        d = [list(np.roll(c[0], b)), list(np.roll(c[1], b))]
    else:
        new_array = np.array([number for number in range(0, a)])
        c = np.array_split(new_array, len(new_array) / (a // 2))
        d = [list(np.roll(c[0], b)), list(np.roll(c[1], b))]
    return d
