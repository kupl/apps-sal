def excluding_vat_price(price):
    return price and round(price / 1.15, 2) or -1
