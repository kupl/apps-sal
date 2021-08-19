def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Happy Coding! ;)
    distance_in_tank = mpg * fuel_left
    if (distance_in_tank >= distance_to_pump):
        return True
    else:
        return False
