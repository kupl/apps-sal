import re
def isDigit(s):
    return re.match(r'^(-?)(([0-9]+\.[0-9]+)|([0-9]+))$',s) is not None
