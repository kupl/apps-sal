def repeat_it(string: str, n: int) -> str:
    """ Get string that repeats the input string `n` number of time. """
    if type(string) is str:
        return string * n
    else:
        return 'Not a string'
