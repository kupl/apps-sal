from decimal import Decimal, ROUND_HALF_UP


def calculate_time(battery, charger):
    n = 2.6 * battery / 1000 * 500 / charger
    return float(Decimal(str(n)).quantize(Decimal('1.23'), rounding=ROUND_HALF_UP))
