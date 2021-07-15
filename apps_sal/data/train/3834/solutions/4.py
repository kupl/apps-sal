def palin(a, b):
    base = str(10**((a - 1) // 2) + b - 1)
    return int(base + base[::-1][a % 2:])
