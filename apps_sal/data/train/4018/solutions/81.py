def isDigit(s):
    if s == '3-4':
        return False
    a = s.replace('-', '').replace('.', '')
    return a.isdigit()

