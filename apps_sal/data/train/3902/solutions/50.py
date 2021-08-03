def duty_free(price, discount, holiday_cost):
    disc = price * discount / 100
    duty_free = holiday_cost // disc
    return duty_free
