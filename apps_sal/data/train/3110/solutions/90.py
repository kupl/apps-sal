def two_decimal_places(n):
    return round(round(n, 2) + 0.01 * (n * 1000 % 10 == 5), 2)
