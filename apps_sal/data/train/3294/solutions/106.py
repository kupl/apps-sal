def converter(mpg):
    """Converts mile/gallon to kilometre/litre."""

    # constants
    mile_to_kilometre = 1.609344
    gallon_to_litre = 4.54609188

    # make some calculations
    formula = mpg * (mile_to_kilometre / gallon_to_litre)

    # round the result
    result = round(formula, 2)

    return result
