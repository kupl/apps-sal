def converter(mpg: int) -> float:
    """ Convert miles per imperial gallon into kilometers per liter. """
    return round(mpg / (4.54609188 / 1.609344), 2)
