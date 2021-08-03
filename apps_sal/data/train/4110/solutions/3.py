from math import ceil


def matrixfy(s):
    if not s:
        return "name must be at least one letter"
    n = ceil(len(s)**.5)
    return [list(s[x:x + n].ljust(n, '.')) for x in range(0, n * n, n)]
