def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg*fuel_left>=distance_to_pump:
        res = True
    else:
        res = False
    return res
