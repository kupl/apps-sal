def excluding_vat_price(price):
    VAT = 15
    return round(price / (100 + VAT) * 100, 2) if price else -1
