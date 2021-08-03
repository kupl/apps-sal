import math


def fuel_price(litres, price_per_liter):

    if litres < 2:
        return litres * price_per_liter

    discount = 0.05 * (math.floor(litres / 2))

    if discount > 0.25:
        discount = 0.25

    return litres * (price_per_liter - discount)
