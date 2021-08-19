def matrixfy(s):
    n = -int(-len(s) ** 0.5 // 1)
    return list(map(list, zip(*[iter(s.ljust(n * n, '.'))] * n))) or 'name must be at least one letter'
