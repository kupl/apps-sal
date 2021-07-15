def fib_rabbits(n, b):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x * b + y
    return x
