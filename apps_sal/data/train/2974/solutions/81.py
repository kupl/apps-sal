def excluding_vat_price(price):
    return -1 if not price else round(100 * price / 115, 2)
