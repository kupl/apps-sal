def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    distance_to_pump = int(distance_to_pump)
    mpg = int(mpg)
    fuel_left = int(fuel_left)
    result = False

    if fuel_left * mpg >= distance_to_pump:
        result = True

    return(result)

