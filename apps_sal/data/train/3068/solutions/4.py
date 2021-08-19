from collections import ChainMap
from string import ascii_lowercase as al
move = ChainMap(dict(c=-1, o=-1, d=-3, e=-4), dict.fromkeys('aeiou', -5), dict.fromkeys(al, 9))
new = (al[(i + move[c]) % 26] for (i, c) in enumerate(al))
mapping = {c: c if c2 in 'code' else c2 for (c, c2) in zip(al, new)}


def vowel_back(st):
    return ''.join(map(mapping.get, st))
