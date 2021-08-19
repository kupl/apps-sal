def hotpo(n):
    return 1 + hotpo(int(n / 2) if n % 2 == 0 else 3 * n + 1) if n > 1 else 0
