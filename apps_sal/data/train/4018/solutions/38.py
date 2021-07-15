def isDigit(string):
    try:
        return type(float(string)) is float
    except ValueError:
        return False
