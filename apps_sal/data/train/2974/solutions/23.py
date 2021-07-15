def excluding_vat_price(price):
    if price:
        return float(format((price-price*15/115), '.2f'))
    else:
        return -1
