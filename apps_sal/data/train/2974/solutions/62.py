def excluding_vat_price(price):
    if type(price) == int or type(price) == float:
        return round(200/230*price,2)
    else:
        return -1

