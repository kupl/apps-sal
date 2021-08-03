def duty_free(normPrice, discount, holiday_cost):
    return int(holiday_cost / ((normPrice * discount) / 100))
