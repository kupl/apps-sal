def excluding_vat_price(price):
    return round(price - (price * (0.15 / 1.15)), 2) if price else -1
