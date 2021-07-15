def excluding_vat_price(price):
    if price is None:
        return -1
    res = price / 1.15
    return round(res, 2)
