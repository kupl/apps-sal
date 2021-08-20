import numpy as np
from itertools import chain
nums = set(range(1, 10))


def validSolution(board):
    a = np.array(board)
    r = range(0, 9, 3)
    return all((set(v.flatten()) == nums for v in chain(a, a.T, (a[i:i + 3, j:j + 3] for i in r for j in r))))
