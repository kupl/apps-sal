import re


_regex = "[^\(|\)]"


def valid_parentheses(string):
    string = re.sub(_regex, '', string)
    while len(string.split('()')) > 1:
        string = ''.join(string.split('()'))
    return string == ''
