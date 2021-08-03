def duty_free(price, discount, holiday_cost):
    return int(holiday_cost // (price - (price * (1 - (discount / 100)))))
