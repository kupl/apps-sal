def capitalize(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]
