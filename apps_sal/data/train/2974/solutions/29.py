def excluding_vat_price(price):
    if price is None:
        return -1    
    sum = price - (price * (15 / 115))
    if price != None:
        return float('{:.2f}'.format(sum))
