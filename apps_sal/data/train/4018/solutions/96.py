def isDigit(string):
    string = string.strip()
    try:
        num = float(string)
        return True
    except:
        return False
