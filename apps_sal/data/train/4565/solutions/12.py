import re


def replace_dots(str):
    result = ''
    for ch in str:
        if ch == '.':
            result += '-'
        else:
            result += ch
    return result
