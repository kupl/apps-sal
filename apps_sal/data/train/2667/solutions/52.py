def zero_fuel(distance_to_pump, mpg, fuel_left):
    print(distance_to_pump, mpg, fuel_left)
    return True if (distance_to_pump-(mpg*fuel_left)) <= 0 else False
