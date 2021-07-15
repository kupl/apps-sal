def zero_fuel(distance_to_pump, mpg, fuel_left):
    make_it = (mpg * fuel_left)
    if (distance_to_pump <= make_it):
        return True
    else:
        return False
