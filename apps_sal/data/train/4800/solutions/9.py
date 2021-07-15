def hotpo(n, i = 0):
    return i if n == 1 else hotpo(int(n / 2) if n % 2 == 0 else 3 * n + 1, i + 1)
