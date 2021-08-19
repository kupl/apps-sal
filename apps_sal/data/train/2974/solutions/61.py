def excluding_vat_price(price):
    if price == None:
        return -1
    else:
        b = price / 1.15
        c = '%.2f' % b
        return float(c)
