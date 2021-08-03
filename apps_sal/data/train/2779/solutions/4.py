def fib_rabbits(n, b):
    f = [0, 1]
    for _ in range(n - 1):
        f.append(f[-1] + b * f[-2])
    return f[n]
