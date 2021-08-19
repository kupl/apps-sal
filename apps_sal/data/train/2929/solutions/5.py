def factors(n):
    return [[d for d in range(2, int(n ** (1 / p) + 2)) if n % d ** p < 1] for p in (2, 3)]
