def excluding_vat_price(price):
    if price == 0 or price == None:
        return -1
    else:
        return round(100*price/115, 2)
