def zero_fuel(distance_to_pump, mpg, fuel_left):
    if float(distance_to_pump / mpg) <= float(fuel_left):
        return True
    else:
        return False
