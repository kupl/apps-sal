def isDigit(string):
    if string == '':
        return False
    elif string[0] == '-':
        return string.replace('-', '', 1).replace('.', '', 1).isdigit()
    else:
        return string.replace('.', '', 1).isdigit()
