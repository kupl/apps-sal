def excluding_vat_price(price):
    # if price == 0:
    # return -1
    ##p = (price / 1.15)
    # return float("{0:.2f}".format(p))
    # return round(p,2)
    try:
        return round(price / 1.15, 2)
    except TypeError:
        return -1
