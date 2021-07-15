def excluding_vat_price(price):

    if price == None:
        return -1
    
    tax = price - price/1.15
    
    no_tax_price = format(price - tax,".2f")
    
    return float(no_tax_price)
