def zero_fuel(distance_to_pump, mpg, fuel_left):
    fueluse = distance_to_pump / mpg
    if fueluse > fuel_left:
        return False
    else:
        return True
