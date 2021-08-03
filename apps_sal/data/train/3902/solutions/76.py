def duty_free(price, discount, holiday_cost):
    price = price * discount / 100
    bottles = holiday_cost // price
    return bottles
