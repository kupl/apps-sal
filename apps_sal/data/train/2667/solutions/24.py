def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / (mpg * fuel_left) <= 1:
        x = True
        return bool(x)
    else:
        x = False
        return bool(x)
