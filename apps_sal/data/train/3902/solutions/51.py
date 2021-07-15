def duty_free(price, discount, holiday_cost):
  a = int(price) * int(discount) / 100
  return int(holiday_cost / a)
