def xMasTree(n):
    r = ['_' * (n - x//2 - 1) + '#' * x + '_' * (n - x//2 - 1) for x in range(1, n * 2, 2)]
    return r + r[:1] * 2
