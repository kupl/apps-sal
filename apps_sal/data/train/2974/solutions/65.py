def excluding_vat_price(price):
    return -1 if price == '' or price is None else float(str(round(1 / 1.15 * price, 2)))
