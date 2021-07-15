from decimal import Decimal, ROUND_HALF_UP

def two_decimal_places(n):
    return float(Decimal(n).quantize(Decimal('.01'), ROUND_HALF_UP))
