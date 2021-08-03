import re


def replace_dots(str):
    output = ''
    for i in str:
        if i == '.':
            output += '-'
        else:
            output += i
    return output
