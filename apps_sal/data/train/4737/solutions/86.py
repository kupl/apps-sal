def fuel_price(litres, price_per_liter):
    print((litres, price_per_liter, '\n'))  
    for i, discount in enumerate (range(0, 25, 5)):
        print(((i+1)*2,discount/100))                              
        if litres < (i+1)*2: return (price_per_liter - discount/100) * litres
    return (price_per_liter - (discount+5)/100)  * litres

