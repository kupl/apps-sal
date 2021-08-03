def excluding_vat_price(price):

    if price:
        return float("{:.2f}".format(price / 1.15))

    else:
        return -1
