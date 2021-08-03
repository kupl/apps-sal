def isDigit(string):
    try:
        _ = float(string)
    except:
        return False
    return True
