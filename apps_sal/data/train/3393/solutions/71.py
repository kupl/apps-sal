import numpy as np


def list_squared(m, n):
    res = []
    for i in range(m, n + 1):
        factor = []
        for k in range(1, int(i ** (1 / 2)) + 1):
            if i % k == 0:
                if k != i // k:
                    factor = factor + [k, i // k]
                else:
                    factor = factor + [k]
        arr = np.array(factor)
        total = sum(arr ** 2)
        if total == int(total ** (1 / 2)) ** 2:
            res.append([i, total])
    return res
