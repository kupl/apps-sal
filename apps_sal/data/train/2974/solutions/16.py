def excluding_vat_price(price):
    return round(price*20/23,2) if price != None else -1
