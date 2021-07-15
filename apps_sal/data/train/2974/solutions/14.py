def excluding_vat_price(price):
    return float(f"{(price / 1.15):.2f}") if price != None else -1
