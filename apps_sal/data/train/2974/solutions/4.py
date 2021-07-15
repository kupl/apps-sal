def excluding_vat_price(price):
    return round(price / 1.15, 2) if price is not None else -1
