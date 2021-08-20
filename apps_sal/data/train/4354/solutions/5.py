def padovan(n):
    a = b = c = 1
    while n:
        (a, b, c) = (b, c, a + b)
        n -= 1
    return a
