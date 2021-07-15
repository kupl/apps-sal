def excluding_vat_price(price):
    return round(price * 100.0 / 115.0, 2) if price else -1
