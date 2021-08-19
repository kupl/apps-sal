def uni_total(string: str) -> int:
    """ Get the total of all the unicode characters as an int. """
    return sum([ord(_) if _ else 0 for _ in '|'.join(string).split('|')])
