def fib_rabbits(n, b):
    (i, a) = (1, 0)
    for m in range(n):
        (i, a) = (a * b, a + i)
    return a

