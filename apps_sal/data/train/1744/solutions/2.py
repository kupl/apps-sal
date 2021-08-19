def fusc(n):
    (a, b) = (0, 1)
    while n > 0:
        if n & 1:
            a = a + b
        else:
            b = a + b
        n >>= 1
    return a
