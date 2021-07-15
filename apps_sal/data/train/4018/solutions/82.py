def isDigit(s):
    try:
        s = float(s)
        return True
    except ValueError:
        return False
