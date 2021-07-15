def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = mpg * fuel_left
    if a >= distance_to_pump:
        return True
    elif a <= distance_to_pump:
        return False
