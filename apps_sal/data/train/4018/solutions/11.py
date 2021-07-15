def isDigit(string):
    try:
        return isinstance(float(string), float)
    except:
        return False
