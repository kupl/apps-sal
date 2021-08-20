from re import sub


def replace_dots(_str: str) -> str:
    """ Replace all dots in given text by dashes. """
    return sub('\\.', '-', _str)
