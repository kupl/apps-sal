def fuel_price(litres, price_per_litre):
    if litres <2:
        return round(litres*price_per_litre, 2)
    elif 2<=litres < 4:    
        total_cost = litres*(price_per_litre - 0.05)
    elif 4 <= litres < 6:
        total_cost = litres*(price_per_litre - 0.10)
    elif 6 <= litres <8:
        total_cost = litres*(price_per_litre - 0.15)
    elif 8 <= litres < 10:
        total_cost = litres*(price_per_litre - 0.2)
    else:
        total_cost = litres*(price_per_litre - 0.25)
    return round(total_cost, 2)
    
        

