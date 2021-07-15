def isDigit(string):
    try:
        int(string) or float(string)
    except ValueError:
        try:
            float(string)
        except ValueError:
            return False
    return True
