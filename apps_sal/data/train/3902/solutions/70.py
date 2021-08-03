def duty_free(price, discount, holiday_cost):
    dut_price = price - (discount / 100 * price)
    saving = price - dut_price
    bottles = holiday_cost / saving
    return int(bottles)
