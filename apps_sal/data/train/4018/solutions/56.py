def isDigit(string):
    return True if string.lstrip('-').replace(".", "", 1).isdigit() else False


