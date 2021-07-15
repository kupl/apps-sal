def hotpo(n):
    return 1 + hotpo(n//2) if n%2 == 0 else 0 if n == 1 else 1 + hotpo(3*n+1)
