def two_decimal_places(n):
    import decimal
    a = float(decimal.Decimal(str(n)).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP))
    print(a)
    return a
