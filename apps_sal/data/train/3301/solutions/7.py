def even_fib(m):
    a, b = 0, 1
    sum = 0
    while a < m:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    return sum
