def two_by_n(n, k):
    if not n:
        return 0
    if n == 1:
        return k
    if n == 2:
        return 2 * k * (k - 1)
    a1, a2, b, c = k, 0, k * (k - 1), k * (k - 1)
    for i in range(n - 2):
        a1, a2, b, c = (c, b,
                        a1 * (k - 1) * (k - 2) + a2 * ((k - 1)**2 - (k - 2)),
                        c * (k - 1) + b * (k - 2))
    return (b + c) % 12345787
