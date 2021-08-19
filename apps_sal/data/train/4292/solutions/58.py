def string_clean(s):
    """
    Function will return the cleaned string
    """
    a = ''
    for c in s:
        if not c.isdigit():
            a += c
    return a
