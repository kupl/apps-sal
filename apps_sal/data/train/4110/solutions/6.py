from math import ceil
from re import findall


def matrixfy(name):
    if not name:
        return 'name must be at least one letter'
    n = ceil(len(name) ** 0.5)
    name = name.ljust(n * n, '.')
    return [list(s) for s in findall('.' * n, name)]
