def duty_free(price, discount, holiday_cost):
    economia = price - price * (100 - discount) * 0.01
    s = holiday_cost // economia
    return s
