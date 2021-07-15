def zero_fuel(distance_to_pump, mpg, fuel_left):
    miles = mpg * fuel_left
    if distance_to_pump <= miles:
        return True
    else:
        return False
    #Happy Coding! ;)

