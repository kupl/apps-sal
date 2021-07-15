def duty_free(price, discount, holiday_cost):
    newprc = price * (1-discount/100)
    saving = price - newprc
    return holiday_cost//saving
