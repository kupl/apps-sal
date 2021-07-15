def zero_fuel(distance_to_pump, mpg, fuel_left):
  miles = fuel_left * mpg
  return distance_to_pump <= miles
