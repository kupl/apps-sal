def excluding_vat_price(price):
    return round(price*0.86956,2) if price else -1
