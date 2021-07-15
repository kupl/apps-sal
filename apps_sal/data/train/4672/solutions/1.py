import re
from string import ascii_lowercase

def repl(m):
    x = m.group()
    if x.isdigit():
        return ascii_lowercase[int(x)-1]
    else:
        return str(ascii_lowercase.find(x) + 1)

def AlphaNum_NumAlpha(string):
    return re.sub(r'[a-z]|\d+', repl, string)
