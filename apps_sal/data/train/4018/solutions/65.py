def isDigit(string):
    try:
        k = int(string)
    except:
        try:
            k = float(string)
        except:
            k = 'nope'
    return True if type(k)==int or type(k)==float else False 

