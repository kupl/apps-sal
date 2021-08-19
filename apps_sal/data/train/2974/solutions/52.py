def excluding_vat_price(price):
    if price == None:
        result = -1
    else:
        result = price / 1.15
    return round(result, 2)
