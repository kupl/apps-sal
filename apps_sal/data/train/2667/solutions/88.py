def zero_fuel(distance_to_pump, mpg, fuel_left):
    berhasil = mpg * fuel_left
    if berhasil >= distance_to_pump:
        return True
    else:
        return False
