def excluding_vat_price(price):
    try:
        return -1 if price<0 else round(price/1.15,2)
    except:
        return -1
