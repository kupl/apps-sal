def candles(m, n):
    c, r = m, 0
    while m:
        m, r = divmod(m+r, n)
        c += m
    return c

