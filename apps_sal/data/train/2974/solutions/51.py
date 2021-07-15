def excluding_vat_price(p):
    return round(p / 1.15, 2) if p else -1
