def zero_fuel(distance_to_pump, mpg, fuel_left):
    your_fuel = mpg*fuel_left
    if your_fuel >= distance_to_pump:
        return True
    else:
        return False
