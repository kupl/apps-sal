def duty_free(price, discount, holiday_cost):
    dfree = price * discount / 100
    return holiday_cost // dfree
