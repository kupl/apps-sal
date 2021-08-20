import re
import random


def roll(desc, verbose=False):
    if not isinstance(desc, str):
        return False
    ans = re.findall('^(\\d*)d(\\d+)(([+\\-]\\d+)*)$', desc.replace(' ', ''))
    if len(ans) == 0:
        return False
    dct = {i: eval(v) for (i, v) in enumerate(ans[0]) if v}
    dices = {'dice': [1 + random.randrange(dct[1]) for i in range(dct.get(0, 1))], 'modifier': dct.get(2, 0)}
    return dices if verbose else sum(dices['dice']) + dices['modifier']
