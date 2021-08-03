def m(n, l, a, b, c): return n and m(n - 1, l, a, c, b) + [l[c].append(l[a].pop()) or str(l)] + m(n - 1, l, b, a, c) or []
def hanoiArray(n): return (lambda l: str(l) + '\n' + '\n'.join(map(str, m(n, l, 0, 1, 2))))([list(range(n, 0, -1)), [], []])
