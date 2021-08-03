def excluding_vat_price(final_price):
    if final_price == None:
        return -1
    else:
        price = final_price * 100 / 115
        return round(price, 2)
