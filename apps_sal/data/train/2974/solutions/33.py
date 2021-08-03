def excluding_vat_price(price):
    if price == 0:
        return 0
    return round((price / (1 + 0.15)), 2) if price != None else -1
