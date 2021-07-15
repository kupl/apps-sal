def duty_free(price, discount, holiday_cost):
    d = discount / 100
    p = price * d
    return holiday_cost // p

