def isDigit(string):
    try:
        x = list(str(string.strip()))
        if '.' in x:
            return type(float(string.strip())) == float
        else:
            return type(int(string.strip())) == int
    except:
        return False
