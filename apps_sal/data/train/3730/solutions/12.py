def capitalize(s):
    return [''.join([c, c.upper()][i % 2] for i, c in enumerate(s, a)) for a in (1, 0)]
