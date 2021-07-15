def count_subsequences(x, y):
    m,n = len(y), len(x)
    cache = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(n + 1): cache[0][i] = 0
    for i in range(m + 1): cache[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if y[i - 1] == x[j - 1]: cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]
            else: cache[i][j] = cache[i - 1][j]
    return cache[m][n]
