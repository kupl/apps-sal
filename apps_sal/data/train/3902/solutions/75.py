def duty_free(price, discount, holiday_cost):
    norm_price = price * (discount / 100)
    return holiday_cost // norm_price    
