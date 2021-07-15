def duty_free(price, discount, holiday_cost):
    discount_total = price/100 * discount
    result = holiday_cost // discount_total
    return result

