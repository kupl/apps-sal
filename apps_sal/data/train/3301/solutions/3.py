def even_fib(m):
    a, b, c = 0, 1, 0
    while b < m:
        if b % 2 == 0:
            c += b
        a, b = b, a + b
    return c
