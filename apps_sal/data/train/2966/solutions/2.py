import re


def calculate(string):
    (a, b) = map(int, re.findall('\\d+', string))
    if 'lose' in string:
        return a - b
    else:
        return a + b
