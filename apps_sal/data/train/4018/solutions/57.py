def isDigit(string):
    string = string.replace('.','')
    if string:
        if string [0] == '-':
            string = string[1:]
        return string.isnumeric()
    else:
        return False
