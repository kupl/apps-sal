def excluding_vat_price(price):
    if not price:
        return -1
    return round(100 * price / 115, 2)
