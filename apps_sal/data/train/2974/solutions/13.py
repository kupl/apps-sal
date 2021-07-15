def excluding_vat_price(price):
    return -1 if price == None else float('{0:.2f}'.format(price/1.15))

