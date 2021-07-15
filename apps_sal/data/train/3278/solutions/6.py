import re

def string_expansion(s):
    out = []
    for n,chars in re.findall(r'([0-9]?)([a-z]+)', s, re.I):
        out.append(''.join(x*int(n or 1) for x in chars))
    return ''.join(out)

