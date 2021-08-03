def two_decimal_places(n):
    i = n - int(n)
    i = i * 1000
    j = (i)
    j = round(j / 10)
    return int(n) + j / 100
