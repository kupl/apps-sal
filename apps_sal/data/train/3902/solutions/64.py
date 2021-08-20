def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price - price * (1 - 0.01 * discount))
