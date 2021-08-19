def find_key(key):
    n = int(key, 16)
    return next(((k - 1) * (n // k - 1) for k in range(2, int(n ** 0.5) + 1) if n % k == 0))
