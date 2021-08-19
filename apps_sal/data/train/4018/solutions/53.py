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


'\n    try:\n        test = int(string)\n        return True\n    except:\n        print("error")\n    try:\n        test = float(string)\n        return True\n    except:\n        return False\n'
