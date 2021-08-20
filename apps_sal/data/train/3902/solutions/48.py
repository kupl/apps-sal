def duty_free(price, discount, holiday_cost):
    q = 0
    w = 0
    p = 0
    q = price * discount / 100
    w = holiday_cost / q * 10
    return w // 10
