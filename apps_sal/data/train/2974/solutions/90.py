def excluding_vat_price(price):
    if price == 0 or price == None:
        return -1
    return round(price / 1.15, 2)
