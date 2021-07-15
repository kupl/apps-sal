def excluding_vat_price(price):
    return round(price - (-1 * (price / 1.15 - price)), 2) if price else -1
