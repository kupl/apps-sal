def looper(a, z, n):
    return [a] if n == 1 else [a] + [(z - a) / (n - 1) * i + a for i in range(1, n - 1)] + [z]
