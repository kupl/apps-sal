def matrixfy(st):
    if not st:
        return 'name must be at least one letter'
    n = 1
    while n*n < len(st):
        n += 1
    st += '.' * (n*n - len(st))
    return [list(xs) for xs in zip(*[iter(st)]*n)]
