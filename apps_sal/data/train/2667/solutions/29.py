def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump-mpg*fuel_left>0:
        return False
    return True
