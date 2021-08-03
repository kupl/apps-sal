def string_clean(s):
    """
    Function will return the cleaned string
    """
    return ''.join(list([x for x in s if x not in '1234567890']))
