def excluding_vat_price(price):
    try:
        origin = float(round(price / 1.15, 2))
        return origin
    except TypeError:
        return -1
