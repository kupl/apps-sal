import re

KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/* "
MAP      = {c: (i//8, i%8) for i,c in enumerate(KEYBOARD)}


def manhattan(*pts): return 1 + sum( abs(z2-z1) for z1,z2 in zip(*pts))

def toggle(m):
    ups, end = m.group(1), m.group(2)
    off = '*' * bool(end)
    return f'*{ups.lower()}{off}{end}'                # Toggle Shift ON if uppercase presents, and then OFF if lowercase after

def tv_remote(words):
    reWords = re.sub(r'([A-Z][^a-z]*)([a-z]?)', toggle, words)
    return sum( manhattan(MAP[was], MAP[curr]) for was,curr in zip('a'+reWords, reWords))

