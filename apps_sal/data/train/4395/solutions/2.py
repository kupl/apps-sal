import re


def next_higher(v):
    return int(re.sub('(0?1)(1*)(0*)$', '10\\3\\2', f'{v:b}'), 2)
