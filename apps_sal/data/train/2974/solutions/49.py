def excluding_vat_price(price):
    return round(price / 1.15, 2) if type(price) == float or type(price) == int else -1
