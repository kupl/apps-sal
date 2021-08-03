import numpy as np


def make_2d_list(head, row, col):
    return np.array(list(range(head, head + row * col))).reshape(row, col).tolist()
