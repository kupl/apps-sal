import re


def get_derivative(s):
    a, b = map(int, re.sub(r'^(\d+)$', r'\1x^0', re.sub(r'x$', 'x^1', s)).split("x^"))
    return re.sub(r'\^1$|x\^0', '', "{}x^{}".format(a * b, b - 1 * bool(b)))
