def fib_rabbits(n, b):
    if n == 0:
        return 0
    x, y = b, 1
    for _ in range(n - 2):
        x, y = y * b, x + y
    return y
