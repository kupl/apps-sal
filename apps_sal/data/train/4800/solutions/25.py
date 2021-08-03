def hotpo(n, c=0):
    return c if n == 1 else hotpo((n % 2) * (3 * n + 1) + ((n + 1) % 2) * (n // 2), c + 1)
