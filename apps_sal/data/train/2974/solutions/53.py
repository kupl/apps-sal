def excluding_vat_price(price):
    if price :
        result = round(price / 1.15, 2)
    else:
        result = -1
    return result
