def isDigit(strng):
    try:
        float(strng)
        return True
    except ValueError:
        return False
