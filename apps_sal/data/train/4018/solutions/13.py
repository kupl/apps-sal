def isDigit(string):
    try:
        type(float(string.strip()))
    except ValueError:
        return False
    return True
