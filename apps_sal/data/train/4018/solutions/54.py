def isDigit(s):
    try:
        float(s)
        return True
    except:
        pass
    return False
