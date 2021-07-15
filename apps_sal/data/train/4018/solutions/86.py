def isDigit(string):
    try :
        string = string.strip(" ")
        try :k = int(string)
        except: float(string)
        return True
    except:
        return False
