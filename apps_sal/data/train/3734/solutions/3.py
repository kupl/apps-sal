import re
import random

def roll(desc, verbose=False):
    if isinstance(desc, str):
        desc_cleared = re.sub(r'\s', '', desc)
        match = re.match(r'^(\d*)d(\d+)((?:[+-]\d+)*)$', desc_cleared)
        if match:
            (dices, sides, modifiers) = match.groups()
            dices, sides = [int(x) if x else 1 for x in [dices, sides]]
            modifier = eval(modifiers) if modifiers else 0
            rolls = [random.randint(1, sides) for _ in range(dices)]
            return {'dice': rolls, 'modifier': modifier} if verbose else sum(rolls) + modifier
    return False
