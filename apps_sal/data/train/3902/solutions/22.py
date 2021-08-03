def duty_free(price, discount, holiday_cost):
    saving = price - (price - price * discount / 100)
    price = holiday_cost // saving
    return price
