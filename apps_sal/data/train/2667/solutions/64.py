def zero_fuel(dpump, mpg, fuel):

    if (mpg * fuel) >= dpump:
        return True
    else:
        return False
