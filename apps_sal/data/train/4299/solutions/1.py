def is_prime_happy(n):
    return n > 2 and (2 + sum((p * all((p % d for d in range(3, int(p ** 0.5) + 1, 2))) for p in range(3, n, 2)))) % n < 1
