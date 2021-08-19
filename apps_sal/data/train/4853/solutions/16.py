def double_char(s: str) -> str:
    """ Get a string in which each character is repeated once. """
    return ''.join(list(map(lambda _: _ * 2, '|'.join(s).split('|'))))
