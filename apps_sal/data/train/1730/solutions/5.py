def two_by_n(n, k):
    mod = 12345787
    if n == 0: return 0
    elif n == 1: return k
    d = [k, 0, k * (k - 1), k * (k - 1)]
    for i in range(3, n + 1):
        x, y, z, w = d
        d = [z, w, (z * (k - 1) + w * (k - 2)) % mod, (x * (k - 1) * (k - 2) + y * ((k - 2)**2 + k - 1)) % mod]
    return (d[2] + d[3]) % mod
