def string_clean(s):
    """
    Function will return the cleaned string
    """
    return s.translate(str.maketrans('1234567890', '0000000000')).replace('0', '')
