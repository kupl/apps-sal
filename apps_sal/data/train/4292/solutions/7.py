from re import compile
from functools import partial
from string import digits
trans = str.maketrans('', '', digits)


def string_clean(s):
    return s.translate(trans)


string_clean = partial(compile('\\d+').sub, '')
