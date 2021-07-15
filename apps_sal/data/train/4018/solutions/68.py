def isDigit(string):
    try:
        float(string.lstrip('-'))
        return True
    except:
        return False
