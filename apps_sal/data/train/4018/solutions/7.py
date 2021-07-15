def isDigit(string):
    #11ELF
    try:
        int(string)
        return True
    except:
        try:
            float(string)
            return True
        except:
            return False
