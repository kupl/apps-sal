import re

def string_expansion(s):
    return re.sub('\d*?(\d?)(\D*)', lambda m: ''.join(int(m.group(1) or 1) * c for c in m.group(2)), s)
