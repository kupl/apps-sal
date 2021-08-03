def duty_free(price, discount, holiday_cost):
    amount_saved = discount / 100 * price
    return int(holiday_cost / amount_saved)
