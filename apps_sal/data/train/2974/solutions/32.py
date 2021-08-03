def excluding_vat_price(price):
    try:
        x = round(price / 1.15, 2)
    except:
        x = -1
    return x
