def duty_free(price, discount, holiday_cost):
    ma = (price / 100) * discount
    return int(holiday_cost / ma)
