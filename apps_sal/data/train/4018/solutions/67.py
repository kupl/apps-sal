def isDigit(string):
    string = string.strip()
    try:
        float(string)
    except ValueError:
        return False
    return True
