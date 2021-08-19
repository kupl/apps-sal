from collections import Counter


def parse_mana_cost(mana):
    if mana != mana.strip() or [c for c in mana.lower() if c not in '0123456789 wubrg']:
        return None
    return Counter(''.join((parse(w) for w in mana.lower().split())))


def parse(w):
    s = '0'
    while w and w[0].isdigit():
        (s, w) = (s + w[0], w[1:])
    return w + '*' * int(s)
