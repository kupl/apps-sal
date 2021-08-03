def two_by_n(n, k):
    P = 12345787
    if k == 1:
        return 1 if n == 1 else 0
    if n == 1:
        return k
    if n == 2:
        return k * (k - 1) * 2 % P
    f0 = [0] * (n + 1)
    f1 = [0] * (n + 1)
    f0[1] = k
    f1[1] = 0
    f0[2] = k * (k - 1) % P
    f1[2] = k * (k - 1) % P
    for i in range(3, n + 1):
        f0[i] = (f0[i - 1] * (k - 1) + f1[i - 1] * (k - 2)) % P
        f1[i] = (f0[i - 2] * (k - 1) * (k - 2) + f1[i - 2] * (k - 1 + (k - 2) * (k - 2))) % P
    return (f0[n] + f1[n]) % P
