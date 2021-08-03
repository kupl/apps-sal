def excluding_vat_price(price=None):
    return -1 if price is None else round(price / 1.15, 2)
