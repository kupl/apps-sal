def excluding_vat_price(price):
    return round(price * 0.8695652173913043, 2) if price else -1
