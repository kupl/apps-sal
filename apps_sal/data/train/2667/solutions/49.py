def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = mpg * fuel_left
    return a >= distance_to_pump
