import re


def get_free_urinals(urinals):
    if '11' in urinals:
        return -1
    return sum((len(g) + 1) // 2 for g in re.split('0?1+0?', urinals))
