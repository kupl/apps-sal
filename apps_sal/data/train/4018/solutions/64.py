def isDigit(string):
    has_dot = False
    for char in string:
        if char == '.':
            has_dot = True

    if has_dot:
        try:
            digit = float(string)
        except:
            return False
    else:
        try:
            digit = int(string)
        except:
            return False

    return True
