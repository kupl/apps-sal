def isDigit(s):
    try:
        return type(int(float(s))) == int
    except:
        return False
