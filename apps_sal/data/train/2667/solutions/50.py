def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    distance_to_pump = float(distance_to_pump)
    mpg = float(mpg)
    fuel_left = float(fuel_left)
    
    if distance_to_pump > mpg*fuel_left:
        return False
    else:
        return True
