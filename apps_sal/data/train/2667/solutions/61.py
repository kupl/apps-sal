def zero_fuel(distance_to_pump, mpg, gallon_left):
    if mpg * gallon_left >= distance_to_pump:
        return True
    else:
        return False
