def duty_free(price, discount, holiday_cost):
    savings_per_bottle = price * discount / 100

    return holiday_cost // savings_per_bottle  # floor division because discrete units
