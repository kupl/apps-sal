import re

def rep(m):
    t = m.groups()[0]
    return str(int(t)+1).zfill(len(t))
    
def increment_string(strng):
    if len(strng) == 0 or not strng[-1].isdigit():
        return strng + '1'
    return re.sub(r'([0-9]+)$', rep,strng)

