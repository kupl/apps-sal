def isDigit(s):
    try:
        float(s.strip())
    except:
        return False
    else:
        return True
