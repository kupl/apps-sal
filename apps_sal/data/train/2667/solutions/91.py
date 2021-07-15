def zero_fuel(distance_to_pump, mpg, fuel_left):
    fn=distance_to_pump-mpg*fuel_left
    if fn<=0:
        return True
    else:
        return False
