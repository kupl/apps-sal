def isDigit(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def problem(a):
    if isDigit(a):
        return int (a * 50 + 6)
    else:
        return "Error"
