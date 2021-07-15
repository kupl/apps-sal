def excluding_vat_price(price):
    if not price == None:
        return round(price / 1.15, 2)
    return -1
