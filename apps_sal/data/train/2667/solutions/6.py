def zero_fuel(distance_to_pump, mpg, fuel_left):
    res = mpg * fuel_left

    if distance_to_pump <= res:
        return 1
    else:
        return 0
