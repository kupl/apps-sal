def isDigit(string):
    try:
        a = float(string)
    except:
        return False
    else:
        return True


"\n    l = list(string)\n    if l.count('.') != 1 and l.count != 0:\n        return False\n    if l.count('-') != 0:\n        if l.count('-') == 1:\n            if l[0] != '-':\n                return False\n            return False\n"
