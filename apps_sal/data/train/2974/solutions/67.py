def excluding_vat_price(price):
    if type(price) != int and type(price) != float:
        return -1
    else:
        return round((price/1.15),2)

