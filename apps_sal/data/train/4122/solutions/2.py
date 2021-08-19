def sc(s):
    xs = set(s)
    return ''.join((c for c in s if c.swapcase() in xs))
