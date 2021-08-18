def two_decimal_places(n):
    """
    a nightmare in a small package
    """

    x = str(n)

    ptIndx = x.find(".")

    roundingDigit = x[ptIndx + 3]

    o = x[0:ptIndx + 3]

    if int(roundingDigit) <= 4:
        return float(o)
    else:
        return round(float(o) + (-0.01 if x[0] == "-" else 0.01), 2)
