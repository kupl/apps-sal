def duty_free(price, discount, holiday_cost):
    print(price, discount, holiday_cost)
    return holiday_cost // (discount * 0.01 * price)
