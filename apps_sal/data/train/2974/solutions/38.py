def excluding_vat_price(price):
    try : return round(price/1.15, 2)
    except : return -1 # o_O
