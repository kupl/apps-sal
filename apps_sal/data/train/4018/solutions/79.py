def isDigit(string):
    try:
        return True if type(float(string))==float else False
    except:
        return False
