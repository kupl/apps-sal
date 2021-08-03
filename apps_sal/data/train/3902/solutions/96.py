def duty_free(price, discount, holiday_cost):
    price = (price * discount / 100)
    return holiday_cost // price
