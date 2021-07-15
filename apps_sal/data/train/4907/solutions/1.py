def candles(m, n):
    burn = leftover = 0
    while m:
        burn += m
        m, leftover = divmod(leftover + m, n)
    return burn
