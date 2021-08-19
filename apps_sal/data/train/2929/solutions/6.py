def factors(n):
    return [[k for k in range(2, int(n ** (1 / p)) + 1) if not n % k ** p] for p in (2, 3)]
