def zero_fuel(distance_to_pump, mpg, fuel_left):
    return 1 / mpg * distance_to_pump <= fuel_left
