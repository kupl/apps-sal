def duty_free(price, discount, holiday_cost):
  duty_free_cost = price - (price - (price*discount*0.01))
  cost= holiday_cost // duty_free_cost
  return cost
