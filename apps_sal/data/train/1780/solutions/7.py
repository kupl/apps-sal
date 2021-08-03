from functools import reduce
import numpy as np

idx = 0
prods = set([])


def enum(buf, n, min_factor=1):
    nonlocal idx, prods
    if len(buf) < n:
        buf = [0 for i in range(n)]
    if n <= 0:
        prods.add(reduce(lambda x, y: x * y, buf[:idx]))
    else:
        for i in range(min_factor, n + 1):
            buf[idx] = i
            idx += 1
            enum(buf, n - i, i)
            idx -= 1


def part(n):
    nonlocal prods, idx
    buf = []
    enum(buf, n)
    ran = max(prods) - min(prods)
    mean = np.mean(list(prods))
    median = np.median(list(prods))
    prods = set([])
    idx = 0
    return "Range: {} Average: {:.2f} Median: {:.2f}".format(ran, mean, median)
