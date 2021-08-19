def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Happy Coding! ;)
    berhasil = mpg * fuel_left
    if (berhasil >= distance_to_pump):
        return True
    else:
        return False
