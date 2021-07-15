import re

def happy_g(s):
    return not re.search(r'(?<!g)g(?!g)',s)
