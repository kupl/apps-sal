def hotpo(n):
    return 0 if n == 1 else 1 + hotpo(3 * n + 1 if n % 2 else n // 2)
