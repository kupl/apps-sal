def duty_free(price, discount, holiday_cost):
    return int(100 * holiday_cost / (price * discount))
