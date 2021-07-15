def isDigit(string):
    try:
        float(string.strip())
        return True
    except:
        return False
