import re


def vert_mirror(strng):
    x = re.split("\s", strng)
    y = [i[::-1] for i in x]
    return '\n'.join(y)


def hor_mirror(strng):
    x = re.split('\s', strng)
    a = x[::-1]
    return '\n'.join(a)


def oper(fct, s):
    return fct(s)
