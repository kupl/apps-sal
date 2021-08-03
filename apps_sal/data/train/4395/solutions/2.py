import re


def next_higher(v):
    return int(re.sub(r'(0?1)(1*)(0*)$', r'10\3\2', f'{v:b}'), 2)
