import re

def increment_string(s):
    if s.isalpha() or not len(s):
        return s + '1'
    r = re.split(r'(\d+$)', s, flags=re.MULTILINE)
    return f'{r[0]}{(int(r[1]) + 1):0{len(r[1])}}'
