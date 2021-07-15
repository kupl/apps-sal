def mystery(n):
    return [i for i in range(1, n + 1, 2) if not n % i]
