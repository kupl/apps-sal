def zero_fuel(distance_to_pump, mpg, fuel_left):
    required_fuel = distance_to_pump / mpg
    return required_fuel <= fuel_left
