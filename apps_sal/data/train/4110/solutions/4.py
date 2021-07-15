from math import ceil
from itertools import chain, repeat
def matrixfy(st):
    s = ceil(len(st) ** 0.5)
    c = chain(st, repeat('.'))
    return [[next(c) for _ in range(s)] for _ in range(s)] or 'name must be at least one letter'
