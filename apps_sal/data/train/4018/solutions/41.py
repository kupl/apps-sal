def isDigit(string):
    try: 
        str2 = string.strip()
        return str2.isdigit() or abs(int(float(str2))) >= 0
    except TypeError:
        return False
    except ValueError:
        return False
