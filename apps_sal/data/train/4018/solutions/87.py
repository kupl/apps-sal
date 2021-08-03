def isDigit(string):
    is_int = True
    is_float = True
    try:
        int(string)
    except ValueError:
        is_int = False
    try:
        float(string)
    except ValueError:
        is_float = False
    return is_int or is_float
