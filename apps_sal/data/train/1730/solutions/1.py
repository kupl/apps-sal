def two_by_n(n, k):
    MOD = 12345787
    x1, x2 = [0, k, k * (k - 1)], [0, 0, k * (k - 1)]
    for _ in range(3, n + 1):
        y1 = (x1[-1] * (k - 1) + x2[-1] * (k - 2)) % MOD
        y2 = (x1[-2] * (k - 1) * (k - 2) + x2[-2] * ((k - 2) * (k - 2) + (k - 1))) % MOD
        x1.append(y1)
        x2.append(y2)
    return (x1[n] + x2[n]) % MOD
