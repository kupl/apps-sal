def excluding_vat_price(price):
    if price == None:
        return -1
    something = price / (1 + 15 / 100)
    return round(something, 2)
