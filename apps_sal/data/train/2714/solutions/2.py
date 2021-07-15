import re

water = re.compile('water|wet|wash', flags=re.I)
slime = re.compile("slime|i don't know", flags=re.I)

def bucket_of(said):
    w = water.search(said)
    s = slime.search(said)
    if w and s:
        return 'sludge'
    elif w:
        return 'water'
    elif s:
        return 'slime'
    else:
        return 'air'
