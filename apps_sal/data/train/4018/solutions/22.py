def isDigit(string):
    import re
    string = string.strip()
    return bool(re.match('^-?\\d*\\.{0,1}\\d+$', string))
