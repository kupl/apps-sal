import re
def process(s):
    if type(s) is not str:
        return ''
    elif re.search(r'[^A-Z]', s, re.I):
        return ''
    else:
        return s.upper()
    
def compare(s1,s2):
    a, b = process(s1), process(s2)
    return sum([ord(c) for c in a]) == sum([ord(c) for c in b])
