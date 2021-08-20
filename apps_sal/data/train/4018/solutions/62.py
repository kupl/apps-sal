def isDigit(string):
    clean_string = string.strip()
    if string == '-0':
        return True
    print(clean_string)
    try:
        if str(int(clean_string)) == clean_string:
            return True
    except:
        pass
    try:
        if str(float(clean_string)) == clean_string:
            return True
    except:
        return False
