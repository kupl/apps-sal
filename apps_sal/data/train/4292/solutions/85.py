def string_clean(s):
    """
    Function will return the cleaned string
    """
    st = [x for x in s if not x.isdigit()]
    return ''.join(st)
