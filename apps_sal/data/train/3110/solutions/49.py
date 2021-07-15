from decimal import Decimal
def two_decimal_places(n):
    return  float(Decimal(n).quantize(Decimal("0.01")))
