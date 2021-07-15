def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return 1
    elif mpg * fuel_left < distance_to_pump:
        return 0
