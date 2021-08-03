def duty_free(price, discount, holiday_cost):
    saved = (price * discount) / 100
    price = holiday_cost // saved
    return price
