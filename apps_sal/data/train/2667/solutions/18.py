def zero_fuel(distance_to_pump, mpg, fuel_left):
    total = mpg * fuel_left
    if distance_to_pump <= total:
        return True
    return False
