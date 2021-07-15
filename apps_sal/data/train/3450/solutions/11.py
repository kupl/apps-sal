def array(string: str) -> str:
    """ Remove first and last character of the string. """
    array = string.split(",")
    if len(array) > 2:
        return " ".join(array[1:-1])
