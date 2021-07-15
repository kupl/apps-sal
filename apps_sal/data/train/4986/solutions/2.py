def sumrange(n):
    return (n - 1) * n / 2
def f(n, m):
    n, m = int(n), int(m)
    return (n / m) * sumrange(m) + sumrange(n % m + 1)
