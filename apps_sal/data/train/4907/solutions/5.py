def candles(m, n):
    c = m
    while m >= n:
        a, b = divmod(m, n)
        c += a
        m = a + b
    return c
