from functools import partial
from re import compile
REGEX = partial(compile('(.)\\1(\\1+)').sub, '\\1\\1[\\2]')


def string_parse(string):
    return REGEX(string) if type(string) == str else 'Please enter a valid string'
