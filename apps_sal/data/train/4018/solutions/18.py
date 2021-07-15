def isDigit(str):
    try:
        float(str)
    except ValueError:
        return False
    return True 

