def excluding_vat_price(price):
    if price != None:
        val = float(price) / 1.15
        return round(val, 2)
    return -1
