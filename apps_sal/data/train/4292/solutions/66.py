def string_clean(s):
    """
    Function will return the cleaned string
    """
    liste = list(s)
    el = []
    for elem in liste:
        if elem in '1234567890':
            pass
        else:
            el.append(elem)
    return ''.join(el)
