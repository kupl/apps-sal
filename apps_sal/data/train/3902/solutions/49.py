def duty_free(price, discount, holiday_cost):
    cst = holiday_cost // (discount / 100 * price)
    return cst
