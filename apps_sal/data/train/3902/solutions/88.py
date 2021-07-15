def duty_free(price, discount, holiday_cost):
    n = int(holiday_cost / (price * (discount/100))) 
    return n
    



