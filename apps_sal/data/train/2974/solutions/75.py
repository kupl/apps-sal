def excluding_vat_price(price):
    if price == None:
        return -1
    return round(100 * price / 115, 2)
