def logistic_map(n, m, x, y):
    co = [[i, j] for i, j in zip(y, x)]
    return [[min([abs(k - i) + abs(l - j) for k, l in co]) if co else None for j in range(n)] for i in range(m)]
