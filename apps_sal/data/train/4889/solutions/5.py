import numpy as np
from collections import deque


def max_hexagon_beam(n: int, seq: tuple):
    max_len = n * 2 - 1

    mat = [0] * max_len**2
    hexag_1 = np.zeros((max_len, max_len))
    hexag_2 = np.zeros((max_len, max_len))
    for i in range(0, len(mat)):
        mat[i] = seq[i % (len(seq))]

    for i in range(n):
        hexag_1[i][0:n + i] = mat[0:n + i]
        rot = deque(hexag_1[i])
        rot.rotate(n - i - 1)
        hexag_2[i] = np.array(rot)
        mat[0:n + i] = []

    j = 1
    for i in range(n, max_len):
        hexag_1[i][j:] = mat[0:max_len - j]
        rot = deque(hexag_1[i])
        rot.rotate(n - i - 1)
        hexag_2[i] = np.array(rot)
        mat[0:max_len - j] = []
        j += 1

    horiz = hexag_1.sum(axis=1)
    diag_1 = hexag_1.sum(axis=0)
    diag_2 = hexag_2.sum(axis=0)

    a = [max(horiz), max(diag_1), max(diag_2)]
    return max(a)
