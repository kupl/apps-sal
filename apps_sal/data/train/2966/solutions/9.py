import re


def calculate(string):
    x, y = [int(n) for n in re.findall(r'\d+', string)]
    return x - y + y * 2 * ('gains' in string)
