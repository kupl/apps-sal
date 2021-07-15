def excluding_vat_price(price):
    return float('{:.2f}'.format(price/1.15)) if price else -1
