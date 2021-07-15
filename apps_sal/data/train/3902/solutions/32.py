def duty_free(price, discount, holiday_cost):
    total_discount = price * discount / 100
    return holiday_cost // total_discount
