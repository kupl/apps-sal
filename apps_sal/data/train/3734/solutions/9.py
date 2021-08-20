import re
from random import randint


def roll(desc, verbose=False):
    if not isinstance(desc, str):
        return False
    match = re.match('^(\\d*)d(\\d+)((?:[+-]\\d+)*)$', desc.replace(' ', ''))
    if match:
        (dices, side, modifiers) = match.groups()
        dices = int(dices) if dices else 1
        modifier = eval(modifiers) if modifiers else 0
        res = list((randint(1, int(side)) for _ in range(dices)))
        return {'dice': res, 'modifier': modifier} if verbose else sum(res) + modifier
    return False
