def hotpo(n, depth=0):
    return depth if n == 1 else hotpo(3 * n + 1 if n % 2 else n / 2, depth + 1)
