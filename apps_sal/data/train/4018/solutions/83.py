def isDigit(s):
    try:
        float(s)
        return True
    except Exception:
        return False
