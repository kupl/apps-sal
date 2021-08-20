def zero_fuel(distance_to_pump, mpg, fuel_left):
    voi_ajaa = mpg * fuel_left
    if voi_ajaa >= distance_to_pump:
        return True
    return False
