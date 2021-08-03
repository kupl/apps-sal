def hotpo(n):
    if n % 2 == 0 and n > 1:
        n = n // 2
        return 1 + hotpo(n)
    if n % 2 == 1 and n > 1:
        n = 3 * n + 1
        return 1 + hotpo(n)
    return 0
