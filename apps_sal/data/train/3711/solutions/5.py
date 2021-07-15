def xMasTree(n):
    n2 = n * 2 - 1
    return [('#' * i).center(n2, '_') for i in range(1, n2 + 1, 2)] + ['#'.center(n2, '_')] * 2
