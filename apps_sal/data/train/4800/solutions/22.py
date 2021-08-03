def hotpo(n, c=0):
    return c if n == 1 else hotpo(3 * n + 1 if n % 2 else n / 2, c + 1)
