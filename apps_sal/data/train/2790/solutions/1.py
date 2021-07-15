import re

def dup(arry):
    return list(map(lambda s: re.sub(r'(\w)\1+', r'\1', s), arry))
