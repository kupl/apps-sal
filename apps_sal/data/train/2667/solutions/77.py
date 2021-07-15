def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    make_it = False;
    get_pump = mpg * fuel_left;
    if (distance_to_pump > get_pump):
        return False;
    elif (distance_to_pump <= get_pump):
        return True;

