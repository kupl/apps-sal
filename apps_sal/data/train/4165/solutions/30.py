def uni_total(string: str) -> int:
    """ Get the total of all the unicode characters as an int. """
    return sum(map(ord, string))
