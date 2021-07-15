def zero_fuel(distance_to_pump, mpg, fuel_left):
    nth=distance_to_pump/mpg
    nth2=fuel_left - nth
    if nth2 >= 0 :
        return True
    else:
        return False
