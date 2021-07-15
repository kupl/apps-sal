def excluding_vat_price(price):
    return round(float(price/1.15), 2) if price != None else -1
