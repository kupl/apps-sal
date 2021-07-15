def two_decimal_places(n):
    z = int(100 * abs(n) + 0.5) / 100.0
    return -z if n < 0 else z

