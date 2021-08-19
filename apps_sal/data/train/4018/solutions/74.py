def isDigit(string):
    if string == '':
        return False
    s = string.split('.')
    if s[0][0] == '-':
        if len(s) == 2:
            if s[0][1:].isdigit() and s[1].isdigit():
                return True
        elif s[0][1:].isdigit():
            return True
    elif len(s) == 2:
        if s[0].isdigit() and s[1].isdigit():
            return True
    elif s[0].isdigit():
        return True
    return False
