def excluding_vat_price(price):
    if price == None:
        return -1
    wo = price / 1.15
    return wo.__round__(2)
