def rounding(n, m):
    return n if n % m == m / 2 else m * round(n / m)
