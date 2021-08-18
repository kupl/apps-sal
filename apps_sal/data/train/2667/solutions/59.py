def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left == 0:
        return distance_to_pump <= mpg
    elif fuel_left > 0:
        m = mpg * fuel_left

    return distance_to_pump <= m
