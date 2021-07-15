def duty_free(price, discount, holiday_cost):
    spb = price * discount / 100
    return holiday_cost // spb
