from itertools import repeat

def double_char(s):
    return ''.join([x for item in s for x in repeat(item, 2)])
