def shortest_arrang(n):
    k = 1
    while n >= 0:
        n -= k
        k += 1
        (d, m) = divmod(n, k)
        if not m:
            return list(range(d + k - 1, d - 1, -1))
    return [-1]
