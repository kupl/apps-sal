from functools import partial
from re import compile
REGEX1 = partial(compile('(?<=\\w)(?=\\b)').sub, '!!!!')
trans = str.maketrans('AEIOU', '@****')


def gordon(a):
    return REGEX1(a.upper()).translate(trans)
