def isDigit(string):
    try:
        return bool(float(string)) or True
    except:
        return False
