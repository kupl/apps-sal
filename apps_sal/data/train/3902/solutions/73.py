def duty_free(price, discount, holiday_cost):
    savings = price * (discount / 100)
    price = holiday_cost // savings
    return price
