from decimal import *
def two_decimal_places(n):
    return float(Decimal(str(n)).quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN))
