def excluding_vat_price(price):
    if price:
        return round((100 * price) / 115, 2)
    return -1
