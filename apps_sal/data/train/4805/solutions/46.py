def check(seq: list, elem) -> bool:
    """ This function returns true if the array contains the value, false if not. """
    for item in seq:
        if elem == item:
            return True
    return False
