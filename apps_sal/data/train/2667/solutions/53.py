def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Let's just return wether the miles we get for our gallons are more or equal to the distance to the pump.
    return (mpg * fuel_left) >= distance_to_pump
