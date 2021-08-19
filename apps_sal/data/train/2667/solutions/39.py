def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Happy Coding! ;)
    # nearest pump 50 miles
    # avg car runs 25 mpg
    # 2 gal left

    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False
