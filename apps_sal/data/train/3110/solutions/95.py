def two_decimal_places(n):
    if (100 * n) % 1 == 0.5:
        return round(n + 0.01, 2)
    else:
        return round(n, 2)
