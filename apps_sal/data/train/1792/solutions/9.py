def three_by_n(n):
    MOD = 12345787
    f = [[1, 0], [1, 2]]
    g = [[0, 1], [0, 1]]

    for i in range(2, n + 1):
        f[0].append((2 * g[0][i - 1] + f[0][i - 2]) % MOD)
        g[0].append((f[0][i - 1] + g[0][i - 2]) % MOD)

    for i in range(2, n + 1):
        f[1].append((2 * f[0][i - 1] + 2 * g[0][i - 2] + f[1][i - 2] + 2 * g[1][i - 1]) % MOD)
        g[1].append((f[0][i - 2] + g[0][i - 1] + f[1][i - 1] + g[1][i - 2]) % MOD)

    return f[1][n]
