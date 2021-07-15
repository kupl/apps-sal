def excluding_vat_price(price):
    if price:
        return round(price - ((price / (1 + .15) * .15)), 2)
    return -1
