def excluding_vat_price(price):
    if type(price) is None:
        return -1
    else:
        try:
            str(price)
            return round(price / 1.15, 2)
        except:
            return -1
