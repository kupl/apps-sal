def isDigit(string):
    if len(string) == 0 or string[0] not in '-+.0123456789':
        return False
    for char in string[1:]:
        if char not in '.0123456789':
            return False
    return True
