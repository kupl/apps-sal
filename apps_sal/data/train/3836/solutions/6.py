def factors(x):
    return [i for i in range(x, 0, -1) if not x % i] if isinstance(x, int) and x > 0 else -1

