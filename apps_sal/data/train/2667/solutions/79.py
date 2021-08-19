def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Happy Coding! ;)
    fuel_need_it = mpg * fuel_left
    if distance_to_pump <= fuel_need_it:
        return True
    else:
        return False
