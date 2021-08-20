def v(k, n):
    return 1.0 / k * (n + 1) ** (-2 * k)


def doubles(maxk, maxn):
    total = 0.0
    k = 1.0
    while k <= maxk:
        n = 1.0
        while n <= maxn:
            total += v(k, n)
            n += 1
        k += 1
    return total
