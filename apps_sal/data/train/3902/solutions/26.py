def duty_free(price, discount, holiday_cost):
    discounted_price = (price*discount)/100
    return holiday_cost//discounted_price
