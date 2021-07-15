def isDigit(string):
    str = string.strip()
    if len(str) == 0:
        return False
    if str[0] == '-':
        str = str[1:]
    if len(str) == 0:
        return False    
    if str[0] == '.' or str[-1] == '.':
        return False
    digit = [s for s in str if s in '0123456789.']
    return True if len(digit) == len(str) else False
