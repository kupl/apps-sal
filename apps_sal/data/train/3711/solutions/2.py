def xMasTree(n):
    w = 2 * n - 1
    return [('#' * (i < n and 2 * i + 1 or 1)).center(w, '_') for i in range(n + 2)]
