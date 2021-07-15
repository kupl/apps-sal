def excluding_vat_price(price=0):

    if type(price)!=int:
        if type(price)!=float:
            return -1
   
    return round((price/115)*100,2)
