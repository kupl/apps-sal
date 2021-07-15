def string_clean(s):
    """
    Function will return the cleaned string
    """
    return ''.join([i for i in s if not i.isnumeric()])
