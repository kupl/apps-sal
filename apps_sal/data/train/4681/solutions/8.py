def alphabetized(s):
    cs = [(c, i) for i, c in enumerate(s) if c.isalpha()]
    cs = sorted(cs, key=lambda c: (c[0].lower(), c[1]))
    return ''.join(c for c, _ in cs)
