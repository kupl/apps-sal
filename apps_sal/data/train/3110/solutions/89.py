def two_decimal_places(n):
    return round(n + 0.0001,2) if -0.1 > n % 0.05 < 0.1  else round(n,2)
