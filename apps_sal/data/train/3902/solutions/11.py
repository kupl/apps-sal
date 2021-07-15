def duty_free(price, discount, holiday_cost):
  return int(holiday_cost / ((discount / 100) * price))
