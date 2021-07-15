def excluding_vat_price(price):
    return round(float(price or -1.15) / 1.15, 2)
