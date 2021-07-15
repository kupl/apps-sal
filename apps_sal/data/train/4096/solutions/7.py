import re

def valid_parentheses(s):
    try:
        re.compile(s)
    except:
        return False
    return True
