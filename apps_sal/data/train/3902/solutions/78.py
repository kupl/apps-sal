def duty_free(price, discount, holiday_cost):
    return holiday_cost // (discount / 100.0 * price)
