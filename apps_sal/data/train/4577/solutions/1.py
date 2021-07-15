import re

def debug(string):
    return re.sub("bug(?!s)", "", string)
