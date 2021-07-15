def excluding_vat_price(price):
    if price:
        return round(price / 115 * 100, 2)
    else:
        return -1
