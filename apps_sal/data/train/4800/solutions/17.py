def hotpo(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + hotpo(n // 2)
    else:
        return 1 + hotpo(3 * n + 1)
