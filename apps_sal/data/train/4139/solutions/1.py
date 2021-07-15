def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30
