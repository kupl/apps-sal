def hotpo(n, c=0): return c if n == 1 else hotpo(n / 2 if not n % 2 else 3 * n + 1, c + 1)
