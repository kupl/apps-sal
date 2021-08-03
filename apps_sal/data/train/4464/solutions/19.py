def feast(beast, dish):
    """ (str, str) -> bool
    Return true if beast and dish start and end with same char.
    """
    return beast[0] == dish[0] and beast[-1] == dish[-1]
