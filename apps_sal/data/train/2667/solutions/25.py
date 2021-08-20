def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = distance_to_pump * (1 / mpg) - fuel_left
    if a <= 0:
        return True
    else:
        return False
