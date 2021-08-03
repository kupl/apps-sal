def excluding_vat_price(price, vat=15):
    return -1 if price is None else round(price / (1 + vat / 100), 2)
