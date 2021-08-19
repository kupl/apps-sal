def two_decimal_places(n):
    if n * 1000 % 10 < 5:
        return round(n, 2)
    else:
        return round(n + 0.001, 2)
