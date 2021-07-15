def zero_fuel(distance_to_pump, mpg, fuel_left):
    necessary_amount = distance_to_pump/mpg
    if necessary_amount <= fuel_left:
        return True
    else:
        return False

