def factors(n):
    return [[d for d in range(2, int(n ** 0.5) + 1) if n % d ** 2 == 0], [d for d in range(2, int(n ** (1 / 3)) + 1) if n % d ** 3 == 0]]
