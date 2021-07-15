def string_clean(s):
    """
    Function will return the cleaned string
    """
    return "".join(x for x in s if x.isdigit()==False)
