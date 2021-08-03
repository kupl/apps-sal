def duty_free(price, discount, holiday_cost):
    spare = price / 100 * discount
    return int(holiday_cost / spare)
