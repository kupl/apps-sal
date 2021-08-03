def excluding_vat_price(price):
    return round(price - price * 0.1304347826086957, 2) if price != None else -1
