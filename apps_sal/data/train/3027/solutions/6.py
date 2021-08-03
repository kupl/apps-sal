import numpy as np


def is_solved(board):
    n = len(board)
    a = np.arange(n * n, dtype=int).reshape(n, n)
    return a.tolist() == board
