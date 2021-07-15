import re
def isDigit(string):
    try:
        float(string)
        return True
    except ValueError:
        pass
    try:
        int(string)
        return True
    except ValueError:
        pass
    return False

