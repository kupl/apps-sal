def duty_free(price, discount, holiday_cost):
    disc_price = (discount / 100) * price
    return holiday_cost // disc_price
