def hex_to_dec(s):
    x = {c: n for (n, c) in enumerate('ABCDEF', 10)}
    y = [x[c] if c in x.keys() else int(c) for c in s.upper()]
    return sum((n * 16 ** i for (n, i) in zip(y, range(len(y))[::-1])))
