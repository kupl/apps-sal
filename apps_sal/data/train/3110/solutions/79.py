def two_decimal_places(n):
    if int(n * 1000) % 10 == 5 and n > 0:
        n = n + 0.001
    return float('{0:.2f}'.format(n))
