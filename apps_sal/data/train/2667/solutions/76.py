def zero_fuel(distance_to_pump, mpg, fuel_left):
    #if fuel left is less than miles to gallon distance to poump
    if distance_to_pump > (mpg * fuel_left ):
        return False
    else:
        return True

