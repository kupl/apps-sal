from itertools import groupby, zip_longest

def blocks(s):
    groups = groupby(sorted(s, key=lambda c: (c.isdigit(), c.isupper(), c)))
    blocks = zip_longest(*(list(b) for _, b in groups), fillvalue="")
    return '-'.join(
        ''.join(b)
        for b in blocks
    )
