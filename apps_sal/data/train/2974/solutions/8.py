def excluding_vat_price(price):
    return round(20/23*price,2) if price else -1
