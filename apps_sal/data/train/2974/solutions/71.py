def excluding_vat_price(price):
    return -1 if price is None else round(price * 100 / 15 / (1 + 100 / 15), 2)
