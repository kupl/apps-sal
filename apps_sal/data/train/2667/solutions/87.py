def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = fuel_left
    b = mpg
    c = distance_to_pump
    if (a * b) >= c:
        return True
    else:
        return False
