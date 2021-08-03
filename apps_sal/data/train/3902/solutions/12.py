def duty_free(price, discount, holiday_cost):
    return int(round(holiday_cost // (price * discount * 0.01)))
