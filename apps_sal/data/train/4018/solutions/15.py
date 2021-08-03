def isDigit(string):
    try:
        a = float(string)
    except:
        return False
    else:
        return True


"""
    l = list(string)
    if l.count('.') != 1 and l.count != 0:
        return False
    if l.count('-') != 0:
        if l.count('-') == 1:
            if l[0] != '-':
                return False
            return False
"""
