def isDigit(number):
    try:
        test = int(number)
    except:
        try:
            test1 = float(number)
        except:
            return False
    return True
