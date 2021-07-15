def isDigit(string):
    if len(string) < 0:
        return False
    else:
        try:
            float(string)
        except:
            return False
        else:
            return True
