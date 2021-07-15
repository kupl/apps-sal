def rounding(n, m):
    return n if (n / m) % 1 == 0.5 else round(n / m) * m
