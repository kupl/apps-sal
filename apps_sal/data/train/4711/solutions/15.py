def zeros(n):
    c, x = 0, 5
    while n > x:
        c += n // x
        x *= 5
    return c
