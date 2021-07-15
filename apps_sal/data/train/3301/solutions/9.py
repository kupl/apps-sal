def even_fib(m):
    a, b = 0, 1
    summ = 0
    while b < m:
        if b % 2 == 0:
            summ += b
        a,b = b, a + b
    return summ

