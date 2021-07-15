def zero_fuel(distance_to_pump, mpg, fuel_left):
    diff = mpg * fuel_left
    if distance_to_pump <= diff:
        return True
    else:
        return False
