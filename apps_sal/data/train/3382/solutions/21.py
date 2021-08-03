from re import findall


def lowercase_count(string: str) -> int:
    """ Get a counter for total number of lowercase letters in a string. """
    return len(findall("[a-z]", string))
