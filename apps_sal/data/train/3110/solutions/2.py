from decimal import Decimal, ROUND_HALF_UP

def two_decimal_places(n):
  dn = Decimal(str(n)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
  return float(dn)

