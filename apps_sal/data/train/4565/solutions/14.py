import re


def replace_dots(s):
    for char in s:
        if char == '.':
            s = s.replace(char, '-')
    return s
