def isDigit(string):
    if string.isdigit():
        return True
    try:
        float(string)
        return True
    except:
        return False
    else:
        return False
