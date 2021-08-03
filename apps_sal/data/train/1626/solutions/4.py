def solve(k):
    k -= 1
    i, d, p, n, s = 0, 1, 0, 9, 45
    while i + s <= k:
        i += s
        p += n * d
        d += 1
        n = 10 ** d - 10 ** (d - 1)
        s = n * p + n * d * (n + 1) // 2
    k -= i
    i = int((((2 * p + d) ** 2 + 8 * k * d) ** 0.5 - (2 * p + d)) / (2 * d))
    k -= i * p + i * d * (i + 1) // 2
    i, d, s = 0, 1, 9
    while i + s <= k:
        i += s
        d += 1
        n = 10 ** d - 10 ** (d - 1)
        s = n * d
    q, r = divmod(k - i, d)
    return int(str(10 ** (d - 1) + q)[r])
