def excluding_vat_price(price):
    return round(20 / 23 * price, 2) if price is not None else -1
