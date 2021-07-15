import math

def excluding_vat_price(price):
    return round(price / 115 * 100, 2) if price else -1
