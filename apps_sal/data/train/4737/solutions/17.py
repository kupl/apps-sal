def fuel_price(litres, price_per_litre):
    if litres%2 == 0 and 2 <= litres <= 8 :
        discount =  round(litres/2,2)*round(5/100,2) 
    elif litres >= 8:
        discount = 0.25
    else :
        discount = 0
    price = round((price_per_litre - discount)*litres,2)
    return price
