def two_decimal_places(n):
    """
    a nightmare in a small package
    """
    
    # Convert to a string
    x = str(n)
    
    # find the decimal
    ptIndx = x.find(".")
    
    # grab the deciding digit
    roundingDigit = x[ptIndx+3]

    # create the return string
    o = x[0:ptIndx+3]
    
    # return if not rounding up
    if int(roundingDigit)<=4:
        return float(o)
    else:
        # round the result of "rounding", since if you don't you get some ###.###9999999764235761923765 garbage
        return round(float(o) + (-0.01 if x[0]=="-" else 0.01), 2)

    #I can't wait to see more appropriate solutions.

