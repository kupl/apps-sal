def duty_free(price, discount, holiday_cost):
    x = price / 100 * discount
    return int(holiday_cost / x)
