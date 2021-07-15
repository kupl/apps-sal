import re

def string_expansion(s):
    return ''.join(''.join(int(n or '1')*c for c in cc) for n,cc in re.findall(r'(\d?)(\D+)', s))

