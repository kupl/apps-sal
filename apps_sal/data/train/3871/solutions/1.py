import numpy as np

def binary_simulation(s, b):
    a, r = np.fromiter(map(int, s), dtype=np.int), []
    for x in b:
        if x[0] == "Q":
            r.append(str(a[x[1]-1]))
        else:
            i, j = x[1:]
            a[i-1:j] ^= 1
    return r
