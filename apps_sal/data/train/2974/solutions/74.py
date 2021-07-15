def excluding_vat_price(price):
    if not price:
        return -1
    VAT = 0.15
    return round(price / (VAT + 1), 2)
