def excluding_vat_price(price):
    if price != None:
        ergebnis = (price / 1.15)

        return round(ergebnis, 2)
    else:
        return -1
