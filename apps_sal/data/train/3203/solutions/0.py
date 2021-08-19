import re


def parse_mana_cost(mana):
    n = {c: mana.lower().count(c) for c in 'wubrg' if mana.lower().count(c) > 0}
    m = re.split('\\D', mana)
    if sum(n.values()) + sum([len(c) for c in m]) != len(mana):
        return None
    p = sum([int(c) for c in m if c != ''])
    if p > 0:
        n['*'] = p
    return n
