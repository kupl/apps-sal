def isDigit(string):
    try:
        return type(int(float(string))) == int
    except Exception:
        return False
