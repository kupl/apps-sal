def isDigit(string):
    string = string.lstrip(" -").rstrip(" ").replace(".", "", 1)
    return string.isdigit()
