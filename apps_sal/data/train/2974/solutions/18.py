def excluding_vat_price(price):
    if type(price) is int or type(price) is float:
        return round(price / 1.15,2)
    else:
        return -1
