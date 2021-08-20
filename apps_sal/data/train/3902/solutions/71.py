def duty_free(price, discount, holiday_cost):
    first = price * discount / 100
    second = holiday_cost // first
    return second
