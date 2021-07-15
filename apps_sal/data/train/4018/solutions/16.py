def isDigit(string):
    string.strip("-")
    string.strip
    try:
        string = int(string)
        return True
    except ValueError:
        pass
    try:
        string = float(string)
        return True
    except ValueError:
        return False
