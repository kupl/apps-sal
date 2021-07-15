import math

def excluding_vat_price(price):
    if price:
        per = price*15/115
        return round(price-per,2)
    else:
        return -1
