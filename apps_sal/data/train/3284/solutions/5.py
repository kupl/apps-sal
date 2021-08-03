from decimal import *


def two_decimal_places(number):
    return float(Decimal(str(number)).quantize(Decimal('.01'), rounding=ROUND_DOWN))
