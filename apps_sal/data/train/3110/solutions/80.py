def two_decimal_places(n):
    from decimal import Decimal
    return float(Decimal(str(n)).quantize(Decimal('0.00')))
