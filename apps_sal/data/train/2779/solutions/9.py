def fib_rabbits(n, b):
    f = [0] * (n + 10)
    f[1] = 1
    for i in range(2, n + 10):
        f[i] = f[i - 1] + (b * f[i - 2])
    return f[n]
