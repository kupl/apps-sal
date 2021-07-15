import math

def zero_fuel(distance_to_pump, mpg, fuel_left):
    
    x = int(distance_to_pump)
    y = int(mpg)
    z = int(fuel_left)
    p = y * z / x
    if(p >= 1) :
        return True
    else:
        return False
