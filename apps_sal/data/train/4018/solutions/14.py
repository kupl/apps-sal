def isDigit(string: str) -> bool:
    """ Check if given string is a valid number. """
    try:
        float(string.strip())
        return True
    except ValueError:
        return False
