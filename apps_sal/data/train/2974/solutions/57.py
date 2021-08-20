def excluding_vat_price(price):
    if str(price) == 'None':
        return -1
    if price <= 0:
        return -1
    sonuc = price / 1.15
    return round(sonuc, 2)
