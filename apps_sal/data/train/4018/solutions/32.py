def isDigit(string):
    return string.lstrip('+-').isdigit() or string.lstrip('+-').replace('.', '', 1).isdigit()
