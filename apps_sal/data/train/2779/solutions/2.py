def fib_rabbits(n, m):
    a, b = 0, 1
    for i in range(n):
        a, b = b, b + a * m
    return a
