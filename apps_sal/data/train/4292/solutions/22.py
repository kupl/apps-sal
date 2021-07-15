def string_clean(s):
    """
    Function will return the cleaned string
    """
    n = ''
    for i in s: 
        if i not in '0123456789':
            n += i
    return n
