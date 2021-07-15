def isDigit(string):
    try:
        if float(string) + 1.0:
            return True
    except ValueError:
        return False
