def zero_fuel(distance, mpg, gallons):
    bool=False
    mpg=mpg*gallons
    if mpg>=distance:
        bool=True
    return bool
