def fuel_price(litres, price_per_liter):
    dis = list(range(0,26,5))[::-1]
    l = list(range(0,11,2))[::-1]
    
    for i in range(len(l)):
        if litres >= l[i]:
            return round(litres * (price_per_liter - dis[i]/100),2)    
