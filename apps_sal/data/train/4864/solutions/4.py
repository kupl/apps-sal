import re


def remove(stg):
    words = stg.split(' ')
    for (i, group) in enumerate(words):
        (b, w, a) = re.search('(!*)([^!]+)(!*)', group).groups()
        s = min(a, b, key=len)
        words[i] = f'{s}{w}{s}'
    return ' '.join(words)
