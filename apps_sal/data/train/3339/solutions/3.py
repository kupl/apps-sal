def mystery(n):
    return [k for k in range(1, n + 1, 2) if n % k == 0]
