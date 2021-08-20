import numpy as np
import math


def get_candy_position(n, r, c, candy):
    if n < candy:
        return [-1, -1, -1]
    box = np.array([['*'] * c] * r)
    n1 = math.ceil(n / (c * r))
    count = 1
    for i in range(1, n1 + 1):
        b = box.copy()
        for j in range(r - 1, -1, -1):
            for k in range(c - 1, -1, -1):
                if count == candy:
                    return [i, j, k]
                b[j][k] = count
                count += 1
