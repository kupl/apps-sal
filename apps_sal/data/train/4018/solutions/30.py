def isDigit(string):
    return all((i.isdigit() or i == '.' for i in (string[1:] if string[0] == '-' else string))) if string else False
