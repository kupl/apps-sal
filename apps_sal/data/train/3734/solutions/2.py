from regex import findall, match
from random import randint


def roll(desc, verbose=False):
    if not (isinstance(desc, str) and match('^(?: *(\\d*d\\d+|[+-]\\d+))+$', desc)):
        return False
    (dices, modifiers) = ([], 0)
    for x in findall('(?: *(\\d*d\\d+|[+-]\\d+))', desc):
        if 'd' in x:
            (a, b) = (1, int(x[1:])) if x[0] == 'd' else map(int, x.split('d'))
            dices.extend((randint(1, b) for _ in range(a)))
        else:
            modifiers += int(x)
    return {'dice': dices, 'modifier': modifiers} if verbose else sum(dices) + modifiers
