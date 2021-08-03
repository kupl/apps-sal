import re


def is_hollow(x):
    return True if re.match('^(1*)0{3,}\\1$', ''.join('0' if i == 0 else '1' for i in x)) else False
