import math
from functools import reduce


def going(n):
    return math.floor(reduce(lambda r, i: r / float(i) + 1, range(1, n + 1), 0) * 1e6) / 1e6
    # return round(reduce(lambda r, i: r / float(i) + 1, xrange(1, n + 1), 0), 6)
