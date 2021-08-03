import re
from random import randint


def roll(desc, verbose=False):
    if not desc:
        return False
    m = re.match(r'^(\d*)d(\d+)(.*)$', desc)
    if not m:
        return False
    num_dice, sides, modifiers = m.groups()
    try:
        modifier = sum(
            int(a) for a in re.sub(r'([-+])', ' \g<1>', modifiers).split())
    except ValueError:
        return False
    nums = [randint(1, int(sides)) for _ in range(int(num_dice or 1))]
    if verbose:
        return {'dice': nums, 'modifier': modifier}
    return sum(nums) + modifier
