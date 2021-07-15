def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    gallons_to_destination = distance_to_pump / mpg
    return True if gallons_to_destination <= fuel_left else False
