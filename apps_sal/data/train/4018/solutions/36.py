def isDigit(string):
    string = string.replace('0', '').strip()
    try:
        if float(string) or int(string):
            return True
    except:
        if string == '-' or string == '.':
            return True
        return False

