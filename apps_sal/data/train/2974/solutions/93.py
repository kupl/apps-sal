def excluding_vat_price(price):
    return round(100*price/115, 2) if price != None else -1
