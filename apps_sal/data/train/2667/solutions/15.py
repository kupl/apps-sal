def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    result = mpg * fuel_left
    if distance_to_pump <= result:
        return True
    else:
        return False
        
zero_fuel(100, 50, 3)
