def zero_fuel(d, mpg, fuel):
    while d == mpg * fuel or d <= mpg * fuel:
        return True
    else:
        return False
