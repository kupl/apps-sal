def isDigit(string):
    try:
        test = int(string)
        return True
    except:
        pass
    try:
        test = float(string)
        return True
    except:
        return False
        
"""
    try:
        test = int(string)
        return True
    except:
        print("error")
    try:
        test = float(string)
        return True
    except:
        return False
"""
