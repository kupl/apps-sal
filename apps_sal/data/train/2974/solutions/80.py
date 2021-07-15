def excluding_vat_price(price):
    return round(price/1.15, 2) if type(price) in [int,float] else -1
