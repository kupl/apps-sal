def fuel_price(litres, price_per_liter):
    discounted = 0
    if litres < 2:
        return round(litres * price_per_liter, 2)
    elif litres >= 2 and litres < 4:
        discounted = price_per_liter - 0.05
        return round(discounted * litres, 2)
    elif litres >= 4 and litres < 6:
        discounted = price_per_liter - 0.10
        return round(discounted * litres, 2)
    elif litres >= 6 and litres < 8:
        discounted = price_per_liter - 0.15
        return round(discounted * litres, 2)
    elif litres >= 8 and litres < 10:
        discounted = price_per_liter - 0.20
        return round(discounted * litres, 2)
    else:
        discounted = price_per_liter - 0.25
        return round(discounted * litres, 2)
    
        
        
    

