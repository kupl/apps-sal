def even_fib(m):
    a, b, total = 1, 1, 0

    while a < m:
        if a % 2 == 0:
            total += a
        a, b = b, a + b

    return total
