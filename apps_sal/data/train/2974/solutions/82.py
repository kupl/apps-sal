def excluding_vat_price(price):
    return -1 if price == 0 or price == None else round(price / 1.15, 2)
