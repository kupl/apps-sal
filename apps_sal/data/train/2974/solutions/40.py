def excluding_vat_price(price):
    if int == type(price) or float == type(price):
        return round(price / 1.15, 2)
    return -1
