import re

def debug(s):
    return re.sub(r'bug(?!s)', '', s)
