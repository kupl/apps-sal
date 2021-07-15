def isDigit(string):
    string.strip()
    string = string.replace(".","")
    try:
        int(string)
        return True
    except:
        return False


