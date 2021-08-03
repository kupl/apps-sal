def isDigit(n):
    try:
        return type(float(n)) == float
    except:
        return False
