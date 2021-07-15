def isDigit(string):
    new = "".join(string.strip())
    try:
        float(new)
        return True
    except:
        return False

