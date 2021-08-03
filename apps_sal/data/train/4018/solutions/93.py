def isDigit(string):
    string = string.strip()
    try:
        i = float(string)
        return True
    except:
        return False
