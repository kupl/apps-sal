def isDigit(string):
    try:
        return True if float(string) + 1 else False
    except:
        return False
