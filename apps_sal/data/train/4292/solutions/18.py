from re import sub


def string_clean(s: str) -> str:
    """ Get cleaned string. """
    return sub("\d", "", s)
