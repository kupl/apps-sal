def zero_fuel(distance_to_pump: float, mpg: float, fuel_left: float) -> bool:
    gallons_needed = distance_to_gallons(distance_to_pump, mpg)
    rslt = gallons_needed <= fuel_left
    return rslt

def distance_to_gallons(distance_to_pump: float, mpg: float) -> float:
    if mpg == 0:
        return 0
    return distance_to_pump / mpg

