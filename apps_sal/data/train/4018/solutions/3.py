def isDigit(string):
    try:
        string = float(string)
    except ValueError:
        return False

    return True    
