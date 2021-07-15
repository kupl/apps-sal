def duty_free(price, discount, holiday_cost):
    saving = price * discount / 100.0
    return int(holiday_cost / saving)
