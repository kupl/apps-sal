def zero_fuel(distance_to_pump, mpg, fuel_left):
    result=mpg*fuel_left - distance_to_pump
    return True if result >=0 else False
