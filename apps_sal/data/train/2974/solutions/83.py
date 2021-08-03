def excluding_vat_price(p):
    try:
        return round(p / 1.15, 2)
    except:
        return -1
