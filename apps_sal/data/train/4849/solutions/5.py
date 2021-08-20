import re


def my_very_own_split(string, delimiter=None):
    if delimiter == '':
        raise ValueError('empty separator')
    delim_re = re.escape(delimiter) if delimiter is not None else '\\s+'
    for s in getattr(re, 'split')(delim_re, string):
        yield s
