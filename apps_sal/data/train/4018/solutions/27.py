def isDigit(string):
    s = string.replace('-', ' ').strip()
    try:
        s = eval(s)
        return 1
    except:
        return 0
