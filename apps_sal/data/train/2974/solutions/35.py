def excluding_vat_price(price):
    return -1 if price == None else round(100 / 115 * price, 2)
