def zero_fuel(distance_to_pump, mpg, fuel_left):
    return not distance_to_pump > mpg * fuel_left
