def duty_free(price, discount, holiday_cost):
    amount_discount = price / 100 * discount
    result = holiday_cost // amount_discount
    return result

