def excluding_vat_price(price):
    if price == None:
        return -1
    else:
        return round(float(price / 1.15), 2)
