def excluding_vat_price(price):
    if price == 'null' or price == None:
        return -1
    return round(price - (price * (1 - 0.86956521739)), 2)
