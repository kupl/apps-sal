def fusc(n):
    a, b = 0, 1
    while n > 0:
        if n & 1:
            a += b
        else:
            b += a
        n >>= 1
    return a
