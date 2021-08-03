def excluding_vat_price(price):
    if price == None:
        return -1
    return round(price / 115 * 100, 2)
