def excluding_vat_price(price):
    if price == None: return -1
    if price > 0: return round (price/1.15, 2)
    else: return 0
