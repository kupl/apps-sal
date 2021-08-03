def two_by_n(n, k):
    if n == 1:
        return k

    n = n - 1
    m = 12345787
    x1, x2, x3, x4 = 0, 1, (k - 1) * (k - 1), k - 2
    y1, y2, y3, y4 = 1, 0, 0, 1

    while n > 1:
        if n % 2 == 1:
            y1, y2, y3, y4 = (x1 * y1 + x2 * y3) % m, (x1 * y2 + x2 * y4) % m, (x3 * y1 + x4 * y3) % m, (x3 * y2 + x4 * y4) % m
        p, s = x2 * x3, x1 + x4
        x1, x2, x3, x4 = (x1 * x1 + p) % m, x2 * s % m, x3 * s % m, (p + x4 * x4) % m
        n = n // 2

    return k * (x1 * y1 + x2 * y3 + 2 * (k - 1) * (x1 * y2 + x2 * y4)) % m
