def solve(s):
    t = None
    while t != s:
        (t, s) = (s, s.replace('()', ''))
    return -1 if len(s) % 2 else sum((1 + (a == tuple(')(')) for a in zip(*[iter(s)] * 2)))
