def duty_free(price, discount, holiday_cost):
    
    economy_nom = price * discount / 100
    return int(holiday_cost / economy_nom)
