from math import ceil


def matrixfy(name):
    if not name:
        return 'name must be at least one letter'
    n = ceil(len(name) ** 0.5)
    name = list(name.ljust(n * n, '.'))
    return [name[i * n:i * n + n] for i in range(n)]
