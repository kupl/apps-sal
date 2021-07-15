def isDigit(string):
    string.strip()
    try:
        string = float(string)
        return True
    except:
        return False

