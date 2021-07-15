def excluding_vat_price(price):
    if price:
        return round(100 / 115 * price, 2)
    else:
        return -1
