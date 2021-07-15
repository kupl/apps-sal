def excluding_vat_price(price):
    print(price)
    return -1 if price == 0 or price == None else round(float(price) / 1.15, 2)
