def zero_fuel(distance_to_pump, mpg, fuel_left):
    fuel_necessary = distance_to_pump / mpg
    if fuel_left >= fuel_necessary:
        return True
    if fuel_left < fuel_necessary:
        return False
