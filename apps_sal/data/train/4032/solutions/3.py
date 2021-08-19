from decimal import Decimal
import numpy as np


def solve(n):
    a = np.ones(1, dtype=Decimal)
    for i in range(n):
        a = np.append(np.add.accumulate(a), [0])
    return a.sum()
