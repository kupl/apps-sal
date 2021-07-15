def string_clean(s):
    """
    Function will return the cleaned string
    """
    return __import__('re').sub('\d+', '', s)
