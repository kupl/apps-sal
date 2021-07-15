def fuel_price(litres, price_per_liter):
    if 2 <= litres < 4:                                  #if liters are more than 2 and less than 4
        return round(litres*(price_per_liter - 0.05), 2) #return price minus 5 cents/0.05
    if 4 <= litres < 6:                                  #if liters are more or equal 4 and less than 6
        return round(litres*(price_per_liter - 0.1), 2)  #return price minus 10 cents/0.10
    if 6 <= litres < 8:                                  #if liters are more or equal 6 and less than 8
        return round(litres*(price_per_liter - 0.15), 2) #return price minus 15 cents/0.15
    if 8 <= litres < 10:                                 #if liters are more or equal 8 and less than 10
        return round(litres*(price_per_liter - 0.2), 2)  #return price minus 20 cents/0.20
    if litres >= 10:                                     #if liters are more or equal 10
        return round(litres*(price_per_liter - 0.25), 2) #return price minus 25 cents/0.25
