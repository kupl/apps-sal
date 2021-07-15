import re
def lowercase_count(strng):
    r = re.compile(r'[a-z]')
    return len(r.findall(strng))
