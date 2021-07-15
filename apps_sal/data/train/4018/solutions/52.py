def isDigit(string):
    try:
        float(string.strip())
        return 1
    except:
        return 0    
