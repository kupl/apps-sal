def excluding_vat_price(price):
    try:
        return round(price * 100 / 115, 2)
    except:
        return -1
