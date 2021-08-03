def S2N(m, n):
    s = 0
    for x in range(m + 1):
        s += sum(x**y for y in range(n + 1))
    return s
