def pillow(s):
    return any([l == 'n' and r == 'B' for l, r in zip(*s)])
