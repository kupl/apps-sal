def excluding_vat_price(price):
    return -1 if not price else round((price * 100 / 115), 2)
