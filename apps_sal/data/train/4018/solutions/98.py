def isDigit(string):
    string = string.strip(' -')
    try:
        convert = float(string)
        return True
    except:
        return False
