def duty_free(price, discount, holiday_cost):
    per_bottle = (discount / 100) * price
    saving = holiday_cost // per_bottle
    return saving
