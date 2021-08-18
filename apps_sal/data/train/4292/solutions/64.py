def string_clean(s):
    """
    Function will return the cleaned string
    """
    st = ""
    for c in s:
        if not(c.isdigit()):
            st += c
    return st
