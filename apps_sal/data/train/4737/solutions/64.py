import math


def fuel_price(litres, price_per_liter):
    dis = math.floor(litres / 2) * 0.05 if math.floor(litres / 2) * 0.05 <= 0.25 else 0.25
    return round((price_per_liter - dis) * litres, 2)
