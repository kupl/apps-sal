def excluding_vat_price(p):
    return round(p / 1.15, 2) if p is not None else -1
