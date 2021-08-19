import math
from functools import reduce


def going(n):
    return math.floor(reduce(lambda r, i: r / float(i) + 1, range(1, n + 1), 0) * 1000000.0) / 1000000.0
