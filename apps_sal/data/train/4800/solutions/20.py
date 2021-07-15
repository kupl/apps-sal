def hotpo(n):
    if n == 1:
        return 0
    return 1 + hotpo(n/2) if not n%2 else 2 + hotpo((n*3 + 1)/2)
